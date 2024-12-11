from zhipuai import ZhipuAI
import os
import base64
import numpy as np
from PIL import Image
from io import BytesIO
from .settings import load_settings, get_vision_settings

def process_glm4(encoded_image, prompt, config):
    """处理图像并返回GLM4的响应
    
    Args:
        encoded_image: base64编码的图像
        prompt: 提示词
        config: 模型配置信息
    
    Returns:
        str: 模型的响应文本
    """
    try:
        # 初始化客户端
        client = ZhipuAI(api_key=config['api_key'])
        
        # 准备消息
        messages = [
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
                            "url": f"data:image/png;base64,{encoded_image}"
                        }
                    }
                ]
            }
        ]
        
        # 调用API
        response = client.chat.completions.create(
            model=config['model_list'][0],  # 使用配置中的第一个模型
            messages=messages,
            max_tokens=1000,
            temperature=0.8
        )
        
        # 返回结果
        return response.choices[0].message.content
        
    except Exception as e:
        return f"GLM4处理出错: {str(e)}"


class LLMs_Vison_GLM4:
    """已废弃的GLM4视觉节点类，请使用新的统一视觉节点"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "prompt": ("STRING", {"multiline": True, "default": "描述这张图片"}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    CATEGORY = "LLMs"

    def process(self, image, prompt):
        config = get_vision_settings("glm4")
        if not config:
            return ("GLM4配置不存在",)
            
        # 编码图像
        if isinstance(image, np.ndarray):
            image = Image.fromarray(np.clip(image * 255, 0, 255).astype(np.uint8))
        
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        encoded_image = base64.b64encode(buffered.getvalue()).decode()
        
        return (process_glm4(encoded_image, prompt, config),)


class LLMs_Chat_GLM4_Only:
    """GLM4专用聊天节点"""

    @classmethod
    def INPUT_TYPES(cls):
        config = get_vision_settings("glm4")
        if not config:
            model_list = ["glm-4"]
        else:
            model_list = config.get("model_list", ["glm-4"])

        return {
            "required": {
                "prompt": ("STRING", {"default": "你好，你是谁？", "multiline": True}),
                "model": (model_list,),
                "temperature": ("FLOAT", {
                    "default": 0.8,
                    "min": 0.0,
                    "max": 2.0,
                    "step": 0.1
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "chat"
    CATEGORY = "LLMs"

    def chat(self, prompt, model, temperature=0.8):
        try:
            config = get_vision_settings("glm4")
            if not config:
                return ("GLM4配置不存在",)

            client = ZhipuAI(api_key=config['api_key'])
            
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature
            )
            
            return (response.choices[0].message.content,)
            
        except Exception as e:
            return (f"GLM4聊天出错: {str(e)}",)
