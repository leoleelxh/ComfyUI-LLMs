from .LLMs_Chat import LLMs_Chat
from .LLMs_Vision_Unified import LLMs_Vision_Unified
from .LLMs_Vison_GLM4 import LLMs_Vison_GLM4, LLMs_Chat_GLM4_Only
from .LLMs_Vison_Ali import LLMs_Vison_Ali
from .LLMs_Vison_Gemini import LLMs_Vison_Gemini

NODE_CLASS_MAPPINGS = {
    "LLMs Chat": LLMs_Chat,
    "LLMs Vision Unified": LLMs_Vision_Unified,
    "LLMs Vision GLM4 (Deprecated)": LLMs_Vison_GLM4,
    "LLMs Vision Ali (Deprecated)": LLMs_Vison_Ali,
    "LLMs Vision Gemini (Deprecated)": LLMs_Vison_Gemini,
    "LLMs Chat GLM4 Only": LLMs_Chat_GLM4_Only
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LLMs Chat": "LLMs Chat 💬",
    "LLMs Vision Unified": "LLMs Vision Unified 🖼️",
    "LLMs Vision GLM4 (Deprecated)": "LLMs Vision GLM4 (Deprecated) 🚫",
    "LLMs Vision Ali (Deprecated)": "LLMs Vision Ali (Deprecated) 🚫",
    "LLMs Vision Gemini (Deprecated)": "LLMs Vision Gemini (Deprecated) 🚫",
    "LLMs Chat GLM4 Only": "LLMs Chat GLM4 Only 💬"
}
