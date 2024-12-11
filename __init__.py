from .LLMs_Chat import LLMs_Chat
from .LLMs_Vision_Unified import LLMs_Vision_Unified

NODE_CLASS_MAPPINGS = {
    "LLMs Chat": LLMs_Chat,
    "LLMs Vision Unified": LLMs_Vision_Unified
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LLMs Chat": "🤖 LLMs Chat | 智能对话",
    "LLMs Vision Unified": "🎯 LLMs Vision | 图像理解"
}

NODE_DISPLAY_CATEGORY_MAPPINGS = {
    "LLMs Chat": "🌟 LLMs",
    "LLMs Vision Unified": "🎭 LLMs"
}
