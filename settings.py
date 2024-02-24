import os
import pathlib

import yaml

DEFAULT_SETTINGS = {
    "cyberdolphin": {
        "openai": {
            "organisation": "NO ORG",
            "api_key": "NO API KEY",
            "model": "gpt-3.5-turbo"
        },
        "openai_compatible": {
            "organisation": "NO ORG",
            "api_key": "your_key",
            "api_base": 'http://ip:3200'
        },
        "prompts": {
            "example_user_prompt": "{Camel|goldfish|glowing orb},{moss|tree|fern|balloon},{space station|garden shed|glowing laser sword|bowl of petunias|orange taxi|neon sign}",
            "default_prompt": {
                "system": "You are deeply artistic, understanding of concepts like composition, pallete and color theory, and image psychology.",
                "prefix": "Do use objective language. Do not add narrative. Do describe objects visually and in context. \
                Do not describe the purpose of the objects, or any other explanations \"",
                "suffix": '"'
            }
        }
    }
}


def load_settings():
    path = os.path.join(os.path.dirname(__file__), "settings.yaml")
    file_path = pathlib.Path(path)
    if not file_path.exists():
        return DEFAULT_SETTINGS['cyberdolphin']

    with open(path) as settings:
        the_yaml = yaml.safe_load(settings)
    # print(f'LOADED: {the_yaml["cyberdolphin"]}')
    return the_yaml['cyberdolphin']


def api_settings(section: str = "openai"):
    openai_settings = load_settings()['openai_compatible'][section]
    return openai_settings['api_base'], openai_settings['api_key'], openai_settings['organisation']
