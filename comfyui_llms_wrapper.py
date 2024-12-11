from .settings import get_chat_settings

def api_settings(section: str = "default"):
    """保持向后兼容的API设置获取函数"""
    settings = get_chat_settings(section)
    return settings['api_base'], settings['api_key'], settings['organisation']
