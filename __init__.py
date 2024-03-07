
from .LLMs_Chat import CyberdolphinOpenAICompatible
from .LLMs_Vison_Ali import LLMs_Vison_Ali
from .LLMs_Vison_Gemini import LLMs_Vison_Gemini
from .LLMs_Vison_GLM4 import LLMs_Vison_GLM4
from .LLMs_Vison_GLM4 import LLMs_Chat_GLM4_Only


NODE_CLASS_MAPPINGS = {

    "😀 LLMs_Chat": CyberdolphinOpenAICompatible,
    "🖼️ LLMs_Vison_Ali": LLMs_Vison_Ali,
    "🖼️ LLMs_Vison_Gemini": LLMs_Vison_Gemini,
    "🖼️ LLMs_Vison_GLM4": LLMs_Vison_GLM4
    # "😀 LLMs_Chat_GLM4_Only": LLMs_Chat_GLM4_Only

}

NODE_DISPLAY_NAME_MAPPINGS = {

    "CyberDolphin OpenAI Compatible": "😀 LLMs_Chat",
    "LLMs_Vison": "🖼️ LLMs_Vison_Ali",
    "LLMs_Vison_Gemini": "🖼️ LLMs_Vison_Gemini",
    "LLMs_Vison_GLM4": "🖼️ LLMs_Vison_GLM4"
    # "LLMs_Chat_GLM4_Only": "😀 LLMs_Chat_GLM4_Only"


}
