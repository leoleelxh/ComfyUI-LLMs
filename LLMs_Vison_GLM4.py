from zhipuai import ZhipuAI
import os
import base64
import json
from io import BytesIO
from .settings import load_settings
from PIL import Image,  ImageChops
from datetime import datetime
import tempfile
import random
import platform

p = os.path.dirname(os.path.realpath(__file__))
# get path
# 获取项目地址


def get_ZhipuAI_api_key():
    try:
        all_settings = load_settings()
        api_key = all_settings['openai_compatible']['default']['vison_key_GLM4']
    except:
        print("出错啦 Error: API key is required")
        return ""
    return api_key


class LLMs_Vison_GLM4:

    # def __init__(self, api_key=None):

    #     all_settings = load_settings()
    #     self.api_key = all_settings['openai_compatible']['default']['vison_key_GLM4']
    #     if self.api_key is not None:
    #         api_key = self.api_key
    #     print("glm4_key:", api_key)
    # 配置参数

    @classmethod
    def INPUT_TYPES(cls):
        all_settings = load_settings()
        default_model = all_settings['openai_compatible']['default']['vision_model_GLM4']

        return {
            "required": {
                "prompt": ("STRING", {"default": "describe this image", "multiline": True}),
                "image_url": ("STRING", {"default": "https://www.mihoyo.com/_nuxt/img/char3.629df8e.png"}),
                "model_name": (default_model,),  # 选用什么模型
                "api_key":  ("STRING", {"default": get_ZhipuAI_api_key()})
            },
            # "optional": {
            #     "image": ("IMAGE",),
            # }
        }

    # 配置
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("GETPrompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "🐵 ComfyUI-LLMs"

    # def tensor_to_image(self, tensor):
    #     # 确保张量是在CPU上
    #     tensor = tensor.cpu()

    #     # 将张量数据转换为0-255范围并转换为整数
    #     # 这里假设张量已经是H x W x C格式
    #     image_np = tensor.squeeze().mul(255).clamp(0, 255).byte().numpy()

    #     # 创建PIL图像
    #     image = Image.fromarray(image_np, mode='RGB')
    #     return image

    def generate_prompt(self, api_key, image_url, prompt, model_name):

        self.api_key = api_key

        if image_url == None:
            raise ValueError("needs a image")
        # else:
        #     # 转换图像
        #     pil_image = self.tensor_to_image(image)

        #     # 生成临时文件路径
        #     temp_directory = tempfile.gettempdir()
        #     unique_suffix = "_temp_" + \
        #         ''.join(random.choice("abcdefghijklmnopqrstuvwxyz")
        #                 for _ in range(5))
        #     filename = f"image{unique_suffix}.png"
        #     temp_image_path = os.path.join(temp_directory, filename)
        #     # temp_image_url = f"file://{temp_image_path}"

        #     # 根据操作系统选择正确的文件URL格式
        #     if platform.system() == 'Windows':
        #         temp_image_url = f"file://{temp_image_path}"
        #     else:
        #         temp_image_url = f"file:///{temp_image_path}"

        #     temp_image_url = temp_image_url.replace('\\', '/')

        #     # 保存图像到临时路径
        #     pil_image.save(temp_image_path)

        #     messages = [
        #         {
        #             "role": "user",
        #             "content": [
        #                 {"image": temp_image_url},
        #                 {"text": prompt}
        #             ]
        #         }
        #     ]
        #     print("temp_image_url:", temp_image_url)
        #     print("prompt:", prompt)

        if prompt is None:
            raise ValueError("Prompt is required")

        # 判断是否正常传入image和prompt，如果没有的话马上中断
        # Determine if image and prompt are being passed in properly, if not break immediately

        client = ZhipuAI(api_key=api_key)  # 填写APIKey Fill in APIKey
        response = client.chat.completions.create(
            model=model_name,  # 选择需要调用的模型名称  Select model
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url
                            }
                        }
                    ]
                }
            ]
        )
        response = str(response.choices[0].message.content)
        return (response,)  # 传出一定要是列表，这个逗号不能省略


class LLMs_Chat_GLM4_Only:

    # def __init__(self, api_key):
    #     all_settings = load_settings()
    #     self.api_key = all_settings['openai_compatible']['default']['vison_key_glm4']
    #     if self.api_key is not None:
    #         api_key = self.api_key
    #     print("glm4_key:", api_key)

    def __init__(self):
        pass

    # 配置参数
    @classmethod
    def INPUT_TYPES(cls):

        all_settings = load_settings()
        default_model = all_settings['openai_compatible']['default']['vision_model_GLM4']

        return {
            "required": {
                "prompt": ("STRING", {"default": "你好，你是谁呀", "multiline": True}),
                "model_name": (default_model,),  # 选用什么模型
                "api_key":  ("STRING", {  # 输入gpt4v的KEY，Add api_key as an input
                    # get OpenAI API Key
                    "multiline": False,
                    "default": get_ZhipuAI_api_key()

                }),

            }
        }

    # 配置
    # config
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Text",)
    FUNCTION = "generate_prompt"
    CATEGORY = "🐵 ComfyUI-LLMs"

    def generate_prompt(self, api_key, prompt, model_name):

        if api_key:
            self.api_key = api_key
        if not self.api_key:
            raise ValueError("API key is required")

        if prompt is None:
            raise ValueError("Prompt is required")
        # 判断是否正常传入image和prompt，如果没有的话马上中断
        # Determine if image and prompt are being passed in properly, if not break immediately

        client = ZhipuAI(api_key=api_key)           # 填写APIKey Fill in APIKey
        response = client.chat.completions.create(
            model=model_name,                           # 选择需要调用的模型名称  Select model
            messages=[
                {"role": "user", "content": "你好"},
                {"role": "assistant", "content": "我是人工智能助手"},
                {"role": "user", "content": "你叫什么名字"},
                {"role": "assistant", "content": "我叫chatGLM"},
                {"role": "user", "content": prompt}
            ],
        )
        response = str(response.choices[0].message.content)
        return (response,)  # 传出一定要是列表，这个逗号不能省略
