import os
import io
import json
import requests
import torch
import google.generativeai as genai
from io import BytesIO
from PIL import Image
from .settings import load_settings

p = os.path.dirname(os.path.realpath(__file__))


def get_gemini_api_key():
    try:
        all_settings = load_settings()
        api_key = all_settings['openai_compatible']['default']['vison_key_gemini']
    except:
        print("出错啦 Error: API key is required")
        return ""
    return api_key


class LLMs_Vison_Gemini:

    def __init__(self, api_key=None):

        all_settings = load_settings()
        self.api_key = all_settings['openai_compatible']['default']['vison_key_gemini']
        if self.api_key is not None:
            genai.configure(api_key=self.api_key, transport='rest')
        print("gemini_key:", self.api_key)

    @classmethod
    def INPUT_TYPES(cls):
        all_settings = load_settings()
        default_model = all_settings['openai_compatible']['default']['vision_model_gemini']
        return {
            "required": {
                "prompt": ("STRING", {"default": "Describe this image", "multiline": True}),
                "model_name": (default_model,),
                "stream": ("BOOLEAN", {"default": False}),
                # Add api_key as an input
                "api_key": ("STRING", {"default": ""})
            },
            "optional": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "generate_content"

    CATEGORY = "🐵 ComfyUI-LLMs"

    def tensor_to_image(self, tensor):
        # 确保张量是在CPU上
        tensor = tensor.cpu()

        # 将张量数据转换为0-255范围并转换为整数
        # 这里假设张量已经是H x W x C格式
        image_np = tensor.squeeze().mul(255).clamp(0, 255).byte().numpy()

        # 创建PIL图像
        image = Image.fromarray(image_np, mode='RGB')
        return image

    def generate_content(self, prompt, model_name, stream, api_key, image=None):
        if api_key:
            self.api_key = api_key
            genai.configure(api_key=self.api_key, transport='rest')
        if not self.api_key:
            raise ValueError("API key is required")

        model = genai.GenerativeModel(model_name)

        if model_name == 'gemini-pro':
            if stream:
                response = model.generate_content(prompt, stream=True)
                textoutput = "\n".join([chunk.text for chunk in response])
            else:
                response = model.generate_content(prompt)
                textoutput = response.text

        if model_name == 'gemini-pro-vision':
            if image == None:
                raise ValueError("gemini-pro-vision needs image")
            else:
                # 转换图像
                pil_image = self.tensor_to_image(image)

                # 直接使用PIL图像
                if stream:
                    response = model.generate_content(
                        [prompt, pil_image], stream=True)
                    textoutput = "\n".join([chunk.text for chunk in response])
                else:
                    response = model.generate_content([prompt, pil_image])
                    textoutput = response.text

        return (textoutput,)



