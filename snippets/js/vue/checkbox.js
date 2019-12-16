Vue.component('MyCheckbox', {
  template: `
    <span>
      <input type="checkbox" v-model="checked"></input>
    </span>
  `,
  data() {
    return {
      checked: false,
    };
  },
});
