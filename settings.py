import os
import pathlib
import yaml

DEFAULT_SETTINGS = {
    "chatllmleoleexh": {
        "openai_compatible": {
            "default": {
                "api_base": "http://url:3200/v1",
                "organisation": "NONE",
                "api_key": "sk-xxxxxxx",
                "model": ["gpt-3.5-turbo"]
            }
        },
        "vision_models": {
            "openai": {
                "api_key": "sk-xxxxxxx",
                "api_base": "http://url:3200/v1",
                "model_list": ["gpt-4-vision-preview"]
            },
            "glm4": {
                "api_key": "xxxxxx",
                "model_list": ["glm-4v"]
            },
            "ali": {
                "api_key": "sk-xxxxx",
                "model_list": ["qwen-vl-plus"]
            },
            "gemini": {
                "api_key": "AIxxxxxx",
                "model_list": ["gemini-pro-vision"]
            }
        }
    }
}


def load_settings():
    """加载配置文件，如果文件不存在则返回默认配置"""
    path = os.path.join(os.path.dirname(__file__), "settings.yaml")
    file_path = pathlib.Path(path)
    if not file_path.exists():
        return DEFAULT_SETTINGS['chatllmleoleexh']

    with open(path, 'r', encoding='utf-8') as settings:
        the_yaml = yaml.safe_load(settings)
    return the_yaml['chatllmleoleexh']


def get_chat_settings(section: str = "default"):
    """获取聊天配置"""
    settings = load_settings()
    return settings['openai_compatible'][section]


def get_vision_settings(model_type: str):
    """获取视觉模型配置"""
    settings = load_settings()
    return settings['vision_models'].get(model_type)


def api_settings(section: str = "default"):
    """保持向后兼容的API设置获取函数"""
    settings = get_chat_settings(section)
    return settings['api_base'], settings['api_key'], settings['organisation']
