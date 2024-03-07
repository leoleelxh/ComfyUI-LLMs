import os
import io
import json
import requests
import torch
import dashscope
from dashscope import MultiModalConversation
from io import BytesIO
from PIL import Image,  ImageChops
from datetime import datetime
import tempfile
import random
import platform
import hashlib
from .settings import load_settings

p = os.path.dirname(os.path.realpath(__file__))


# def get_vison_api_key():
#     try:
#         config_path = os.path.join(p, 'config.json')
#         with open(config_path, 'r') as f:
#             config = json.load(f)
#         api_key = config["QWENVL_API_KEY"]
#     except:
#         print("出错啦 Error: API key is required")
#         return ""
#     return api_key


class LLMs_Vison_Ali:

    def __init__(self):

        all_settings = load_settings()
        self.api_key = all_settings['openai_compatible']['default']['vison_key_ali']
        # self.api_key = get_qwenvl_api_key()
        if self.api_key is not None:
            dashscope.api_key = self.api_key
        print("key:", self.api_key)

    @classmethod
    def INPUT_TYPES(cls):

        all_settings = load_settings()
        # api_key = [a for a in all_settings['openai_compatible']]
        default_model = all_settings['openai_compatible']['default']['vision_model_ali']
        # dashscope.api_key = api_key

        return {
            "required": {
                "image": ("IMAGE",),
                "prompt": ("STRING", {"default": "Describe this image", "multiline": True}),
                "model_name": (default_model,),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "vison_generation"

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

    def vison_generation(self, image, prompt, model_name, seed):
        if not self.api_key:
            raise ValueError("API key is required")

        if image == None:
            raise ValueError("needs a image")
        else:
            # 转换图像
            pil_image = self.tensor_to_image(image)

            # 生成临时文件路径
            temp_directory = tempfile.gettempdir()
            unique_suffix = "_temp_" + \
                ''.join(random.choice("abcdefghijklmnopqrstuvwxyz")
                        for _ in range(5))
            filename = f"image{unique_suffix}.png"
            temp_image_path = os.path.join(temp_directory, filename)
            # temp_image_url = f"file://{temp_image_path}"

            # 根据操作系统选择正确的文件URL格式
            if platform.system() == 'Windows':
                temp_image_url = f"file://{temp_image_path}"
            else:
                temp_image_url = f"file:///{temp_image_path}"

            temp_image_url = temp_image_url.replace('\\', '/')

            # 保存图像到临时路径
            pil_image.save(temp_image_path)

            messages = [
                {
                    "role": "user",
                    "content": [
                        {"image": temp_image_url},
                        {"text": prompt}
                    ]
                }
            ]

            print("temp_image_url:", temp_image_url)
            print("prompt:", prompt)

            torch.manual_seed(seed)

            response = dashscope.MultiModalConversation.call(
                model=model_name, messages=messages, seed=seed)
            print(response)

            response_json = response
            if 'output' in response_json and 'choices' in response_json['output']:
                choices = response_json['output']['choices']
                if choices and 'message' in choices[0]:
                    message_content = choices[0]['message']['content']
                    if message_content and 'text' in message_content[0]:
                        text_output = message_content[0]['text']
                        # print(text_output)
                    else:
                        print("No text content found.")
                else:
                    print("No message found in the first choice.")
            else:
                print("No choices found in the output.")

            os.remove(temp_image_path)
            # print("remove : done!" )

        return (text_output, )


