from openai import OpenAI
import base64
from PIL import Image
from io import BytesIO

def process_openai(encoded_image, prompt, config):
    """处理图像并返回OpenAI视觉模型的响应
    
    Args:
        encoded_image: base64编码的图像
        prompt: 提示词
        config: 模型配置信息
    
    Returns:
        str: 模型的响应文本
    """
    try:
        # 初始化客户端
        client = OpenAI(
            api_key=config['api_key'],
            base_url=config['api_base']
        )
        
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
            model=config['model_list'][0],
            messages=messages,
            max_tokens=1000
        )
        
        # 返回结果
        return response.choices[0].message.content
        
    except Exception as e:
        return f"OpenAI视觉处理出错: {str(e)}" 