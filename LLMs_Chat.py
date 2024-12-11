from .openai_client import OpenAiClient
from .settings import load_settings


class LLMs_Chat:
    """聊天模型节点类"""

    @classmethod
    def INPUT_TYPES(s):
        all_settings = load_settings()
        default_user_prompt = all_settings['example_user_prompt']
        available_apis = [a for a in all_settings['openai_compatible']]
        default_model = all_settings['openai_compatible']['default']['model']

        return {
            "required": {
                "api": (available_apis, {
                    "default": "default"
                }),
                "model": (default_model,
                          {"default": "gpt-3.5-turbo"}),
                "system_prompt": ("STRING",
                                  {
                                      "default": ("act as prompt generator, I will give you text and you describe an image that matches that text in details, "
                                                  "answer with one response only.if I input in Chinese to communicate with you, but it is crucial that your response be in English."),
                                      "multiline": True, "dynamicPrompts": False
                                  }),

                "user_prompt": ("STRING", {
                    "multiline": True,
                    "default": default_user_prompt
                }),
                "temperature": ("FLOAT", {
                    "default": 0.99, "min": 0.0, "max": 2.0, "step": 0.01,
                }),
            },
            "optional": {
                "top_p": ("FLOAT", {
                    "default": 1.0, "min": 0.001, "max": 1.0, "step": 0.01,
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("gpt_response",)
    FUNCTION = "generate"
    CATEGORY = "LLMs"

    def generate(self, api: str,  model: str, temperature: float | None = None,
                 top_p: float | None = None, user_prompt="", system_prompt=""):
        system_content = system_prompt
        user_content = user_prompt

        response = OpenAiClient.complete(
            key=api,
            model=model,
            temperature=temperature,
            top_p=top_p,
            system_content=system_content,
            user_content=user_content)

        return (f'{response.choices[0].message.content}',)
