from django.contrib.postgres.fields import JSONField
from ruamel import yaml


class InvalidYAMLInput(str):
    pass


class YAMLString(str):
    pass


class YAMLFormField(forms.CharField):
    default_error_messages = {
        "invalid": _("'%(value)s' value must be valid YAML."),
    }
    widget = forms.Textarea

    def to_python(self, value):
        if self.disabled:
            return value
        if value in self.empty_values:
            return None
        elif isinstance(value, (list, dict, int, float, YAMLString)):
            return value
        try:
            converted = yaml.safe_load(value)
        except ValueError:
            raise forms.ValidationError(
                self.error_messages["invalid"],
                code="invalid",
                params={"value": value},
            )
        if isinstance(converted, six.text_type):
            return YAMLString(converted)
        else:
            return converted

    def bound_data(self, data, initial):
        if self.disabled:
            return initial
        try:
            return yaml.safe_loads(data)
        except ValueError:
            return InvalidYAMLInput(data)

    def prepare_value(self, value):
        if isinstance(value, InvalidYAMLInput):
            return value
        return yaml.safe_dump(value, default_flow_style=False)


class JSONFieldAsYaml(JSONField):
    def formfield(self, **kwargs):
        defaults = {"form_class": YAMLFormField}
        defaults.update(kwargs)
        super(JSONFieldAsYaml, self).formfield(**defaults)
