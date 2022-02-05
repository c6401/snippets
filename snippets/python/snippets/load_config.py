from pathlib import Path
from ruamel import yaml
###
config_path = Path('~/.config/____/config.yml').expanduser()

config = {}
if config_path.is_file():
    with config_path.open() as f:
        config = yaml.safe_load(f) or {}
