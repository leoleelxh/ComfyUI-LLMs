import os
import io
import json
import requests
import torch
import dashscope
from dashscope import MultiModalConversation
from io import BytesIO
from PIL import Image, ImageChops
from datetime import datetime
import tempfile
import random
import platform
import hashlib
from .settings import load_settings
import base64

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


def process_ali(encoded_image, prompt, config):
    """处理图像并返回阿里视觉模型的响应
    
    Args:
        encoded_image: base64编码的图像
        prompt: 提示词
        config: 模型配置信息
    
    Returns:
        str: 模型的响应文本
    """
    try:
        # 设置API密钥
        dashscope.api_key = config['api_key']
        
        # 准备消息
        messages = [{
            'role': 'user',
            'content': [
                {'image': f'data:image/png;base64,{encoded_image}'},
                {'text': prompt}
            ]
        }]
        
        print("正在调用阿里视觉API...")
        print(f"使用模型: {config['model_list'][0]}")
        
        # 调用API
        response = MultiModalConversation.call(
            model=config['model_list'][0],
            messages=messages
        )
        
        print(f"API响应状态码: {response.status_code}")
        
        # 检查响应
        if response.status_code == 200:
            try:
                # 从响应中提取文本内容
                if hasattr(response.output, 'choices') and len(response.output.choices) > 0:
                    # 获取第一个选择的消息内容
                    choice = response.output.choices[0]
                    if hasattr(choice, 'message') and hasattr(choice.message, 'content'):
                        # 如果消息内容是列表，获取文本部分
                        if isinstance(choice.message.content, list):
                            for content in choice.message.content:
                                if isinstance(content, dict) and 'text' in content:
                                    result = content['text']
                                    print(f"提取的文本结果: {result}")
                                    return result
                        else:
                            result = choice.message.content
                            print(f"提取的文本结果: {result}")
                            return result
                
                # 如果上述方式无法获取文本，尝试其他方式
                if hasattr(response.output, 'text'):
                    result = response.output.text
                    print(f"提取的文本结果: {result}")
                    return result
                
                # 如果仍然无法获取文本，返回完整的输出
                print("无法提取文本，返回完整输出")
                return str(response.output)
                
            except Exception as e:
                print(f"处理响应时出错: {str(e)}")
                return f"处理响应时出错: {str(e)}"
        else:
            error_msg = f"阿里视觉模型调用失败: {response.status_code} - {response.message if hasattr(response, 'message') else '未知错误'}"
            print(error_msg)
            return error_msg
            
    except Exception as e:
        print(f"阿里视觉API错误详情: {str(e)}")
        print(f"错误类型: {type(e)}")
        if hasattr(e, 'response'):
            print(f"响应内容: {e.response}")
        return f"阿里视觉处理出错: {str(e)}"


# 保留原有的节点类，但标记为废弃
class LLMs_Vison_Ali:
    """已废弃的阿里视觉节点类，请使用新的统一视觉节点"""
    pass


