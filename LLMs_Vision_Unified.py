import os
import yaml
import folder_paths
import numpy as np
import torch
from PIL import Image
import io
import base64

class LLMs_Vision_Unified:
    """统一的视觉模型节点"""
    
    def __init__(self):
        self.config = self._load_config()
        self.model_lists = {}
        # 预先加载所有模型类型的子模型列表
        for model_type in self.config['chatllmleoleexh']['vision_models']:
            self.model_lists[model_type] = self.config['chatllmleoleexh']['vision_models'][model_type]['model_list']
    
    @classmethod
    def INPUT_TYPES(cls):
        """定义节点输入类型"""
        config = cls._load_config_static()
        vision_models = config['chatllmleoleexh']['vision_models']
        
        # 获取所有模型类型
        model_types = list(vision_models.keys())
        
        # 获取所有可用的子模型
        all_models = []
        for model_type in model_types:
            all_models.extend(vision_models[model_type]['model_list'])
        
        return {
            "required": {
                "image": ("IMAGE",),
                "model_type": (model_types,),
                "model": (all_models,),  # 所有可用的子模型
                "prompt": ("STRING", {
                    "multiline": True, 
                    "default": "Please provide a detailed description of this image, including:\n- The main subject(s) and their appearance\n- The setting and environment\n- Colors, lighting, and visual elements\n- Any notable details or unique features\n- The overall mood and atmosphere\n\nDescribe as if you are explaining the image to someone who cannot see it."
                }),
            }
        }
    
    @classmethod
    def _load_config_static(cls):
        """静态方法加载配置"""
        config_path = os.path.join(folder_paths.base_path, "custom_nodes", "ComfyUI-LLMs", "settings.yaml")
        if not os.path.exists(config_path):
            return {
                "chatllmleoleexh": {
                    "vision_models": {
                        "openai": {"model_list": ["gpt-4-vision-preview"]},
                        "glm4": {"model_list": ["glm-4v"]},
                        "ali": {"model_list": ["qwen-vl-plus"]},
                        "gemini": {"model_list": ["gemini-pro-vision"]}
                    }
                }
            }
            
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "process_image"
    CATEGORY = "LLMs"

    def _load_config(self):
        """加载配置文件"""
        return self._load_config_static()
    
    def _get_vision_config(self, model_type):
        """获取指定视觉模型的配置"""
        try:
            return self.config['chatllmleoleexh']['vision_models'][model_type]
        except KeyError:
            raise ValueError(f"未找到模型类型 {model_type} 的配置")
    
    def _encode_image(self, image_tensor):
        """将图像编码为base64字符串"""
        if isinstance(image_tensor, torch.Tensor):
            image_tensor = image_tensor.cpu()
            image = Image.fromarray(np.clip(image_tensor.squeeze().numpy() * 255, 0, 255).astype(np.uint8))
        elif isinstance(image_tensor, np.ndarray):
            image = Image.fromarray(np.clip(image_tensor * 255, 0, 255).astype(np.uint8))
        else:
            raise ValueError("不支持的图像格式")
        
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()
    
    def process_image(self, image, model_type, model, prompt):
        """处理图像并返回描述"""
        model_config = self._get_vision_config(model_type)
        encoded_image = self._encode_image(image)
        
        # 验证所选模型是否属于当前模型类型
        if model not in self.model_lists[model_type]:
            available_models = ", ".join(self.model_lists[model_type])
            return (f"错误：所选模型 {model} 不属于 {model_type} 类型。可用的模型有：{available_models}",)
        
        # 更新配置中的模型
        model_config = dict(model_config)
        model_config['model_list'] = [model]
        
        # 根据不同模型类型调用相应的API
        try:
            if model_type == "openai":
                from .LLMs_Vision_OpenAI import process_openai
                return (process_openai(encoded_image, prompt, model_config),)
            elif model_type == "glm4":
                from .LLMs_Vison_GLM4 import process_glm4
                return (process_glm4(encoded_image, prompt, model_config),)
            elif model_type == "ali":
                from .LLMs_Vison_Ali import process_ali
                return (process_ali(encoded_image, prompt, model_config),)
            elif model_type == "gemini":
                from .LLMs_Vison_Gemini import process_gemini
                return (process_gemini(encoded_image, prompt, model_config),)
            else:
                return (f"不支持的模型类型: {model_type}",)
        except Exception as e:
            return (f"处理图像时出错: {str(e)}",)

NODE_CLASS_MAPPINGS = {
    "LLMs_Vision_Unified": LLMs_Vision_Unified
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LLMs_Vision_Unified": "LLMs Vision Unified 🖼️"
} 