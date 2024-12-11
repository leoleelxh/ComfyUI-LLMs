# ComfyUI LLMs Extension

A ComfyUI extension that supports various Large Language Models (LLMs) and Vision Language Models (VLMs), providing a unified interface and simple configuration.

[English](#english) | [中文](#chinese)

<a name="english"></a>
## ✨ Features

- 🤖 Support for multiple LLM chat models
- 🎯 Unified vision model interface with multiple VLM support
- 🔄 Dynamic model switching
- 🌐 Bilingual interface (English/Chinese)
- ⚙️ Simple configuration

## 📦 Installation

1. Navigate to ComfyUI's custom_nodes directory
```bash
cd ComfyUI/custom_nodes
```

2. Clone the repository
```bash
git clone https://github.com/leoleexh/ComfyUI-LLMs
```

3. Install dependencies
```bash
cd ComfyUI-LLMs
pip install -r requirements.txt
```

## ⚙️ Configuration

### Basic Setup

1. Copy the configuration template
```bash
cp settings.yaml.sample settings.yaml
```

2. Edit `settings.yaml` to configure your API keys and model settings

### Detailed Configuration

The configuration file structure is as follows:

```yaml
chatllmleoleexh:
  # OpenAI Compatible Interface Configuration
  openai_compatible:
    default:
      api_base: "http://your-api-endpoint:3200/v1"  # API endpoint
      organisation: "NONE"                          # Organization ID (optional)
      api_key: "your-api-key"                      # API key
      model:                                       # Supported models
        - "gpt-3.5-turbo"
        - "gpt-4"
        # Other supported models...

  # Vision Models Configuration
  vision_models:
    # OpenAI Vision Model
    openai:
      api_key: "your-openai-key"
      api_base: "http://your-api-endpoint:3200/v1"
      model_list:
        - "gpt-4-vision-preview"
    
    # Zhipu GLM4 Vision Model
    glm4:
      api_key: "your-glm4-key"
      model_list: 
        - "glm-4v"
        - "glm-4"
    
    # Alibaba Qwen Vision Model
    ali:
      api_key: "your-ali-key"
      model_list:
        - "qwen-vl-plus"
        - "qwen-vl-max"
    
    # Google Gemini Vision Model
    gemini:
      api_key: "your-gemini-key"
      model_list:
        - "gemini-pro-vision"

  # Prompt Templates Configuration
  prompt_templates:
    default:
      system: "System prompt"
      prefix: "Prefix prompt"
      suffix: "Suffix prompt"
```

### Model Support

1. **OpenAI and Compatible Models**
   - Standard OpenAI API support
   - Third-party compatible interfaces (e.g., One API)
   - Multiple models and endpoints configuration

2. **Vision Model Support**
   - OpenAI GPT-4V
   - Zhipu GLM-4V
   - Alibaba Qwen VL
   - Google Gemini

### API Key Acquisition

- OpenAI: https://platform.openai.com/
- Zhipu GLM: https://open.bigmodel.cn/
- Alibaba Qwen: https://dashscope.aliyun.com/
- Google Gemini: https://makersuite.google.com/

## 🎯 Usage

### Chat Function
1. Find `🤖 LLMs Chat` in the node list
2. Configure model parameters
3. Input conversation content

### Image Understanding
1. Find `🎯 LLMs Vision` in the node list
2. Select the vision model to use
3. Connect image input
4. Run to get image description

## 🔄 Changelog

See [CHANGELOG.md](CHANGELOG.md)

## 📝 Notes

- Ensure API keys are configured correctly
- Some models may require proxy access
- Stable network connection recommended
- Be aware of API rate limits

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📄 License

MIT License

---

<a name="chinese"></a>
# ComfyUI LLMs 扩展

ComfyUI的LLM扩展，支持多种大语言模型和视觉语言模型，提供统一的接口和简单的配置方式。

## ✨ 功能特点

- 🤖 支持多种LLM模型的对话功能
- 🎯 统一的视觉模型接口，支持多种视觉语言模型
- 🔄 动态模型切换
- 🌐 支持中英文双语界面
- ⚙️ 简单的配置方式

## 📦 安装方法

1. 进入ComfyUI的custom_nodes目录
```bash
cd ComfyUI/custom_nodes
```

2. 克隆仓库
```bash
git clone https://github.com/leoleexh/ComfyUI-LLMs
```

3. 安装依赖
```bash
cd ComfyUI-LLMs
pip install -r requirements.txt
```

## ⚙️ 配置说明

### 基本配置

1. 复制配置文件模板
```bash
cp settings.yaml.sample settings.yaml
```

2. 编辑 `settings.yaml` 文件，配置您的API密钥和模型设置

### 详细配置说明

配置文件结构如下：

```yaml
chatllmleoleexh:
  # OpenAI兼容接口配置
  openai_compatible:
    default:
      api_base: "http://your-api-endpoint:3200/v1"  # API端点
      organisation: "NONE"                          # 组织ID（可选）
      api_key: "your-api-key"                      # API密钥
      model:                                       # 支持的模型列表
        - "gpt-3.5-turbo"
        - "gpt-4"
        # 其他支持的模型...

  # 视觉模型配置
  vision_models:
    # OpenAI视觉模型
    openai:
      api_key: "your-openai-key"
      api_base: "http://your-api-endpoint:3200/v1"
      model_list:
        - "gpt-4-vision-preview"
    
    # 智谱GLM4视觉模型
    glm4:
      api_key: "your-glm4-key"
      model_list: 
        - "glm-4v"
        - "glm-4"
    
    # 阿里通义千问视觉模型
    ali:
      api_key: "your-ali-key"
      model_list:
        - "qwen-vl-plus"
        - "qwen-vl-max"
    
    # Google Gemini视觉模型
    gemini:
      api_key: "your-gemini-key"
      model_list:
        - "gemini-pro-vision"

  # 提示词模板配置
  prompt_templates:
    default:
      system: "系统提示词"
      prefix: "前缀提示词"
      suffix: "后缀提示词"
```

### 模型支持说明

1. **OpenAI及兼容模型**
   - 支持标准OpenAI接口
   - 支持第三方兼容接口（如One API）
   - 可配置多个模型和接口

2. **视觉模型支持**
   - OpenAI GPT-4V
   - 智谱 GLM-4V
   - 阿里通义千问
   - Google Gemini

### API密钥获取

- OpenAI: https://platform.openai.com/
- 智谱GLM: https://open.bigmodel.cn/
- 阿里通义千问: https://dashscope.aliyun.com/
- Google Gemini: https://makersuite.google.com/

## 🎯 使用方法

### 聊天功能
1. 在节点列表中找到 `🤖 LLMs Chat | 智能对话`
2. 配置模型参数
3. 输入对话内容

### 图像理解功能
1. 在节点列表中找到 `🎯 LLMs Vision | 图像理解`
2. 选择要使用的视觉模型
3. 连接图像输入
4. 运行获取图像描述

## 🔄 更新日志

详见 [CHANGELOG.md](CHANGELOG.md)

## 📝 注意事项

- 请确保API密钥配置正确
- 部分模型可能需要代理访问
- 建议使用稳定的网络环境
- 注意API调用频率限制

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License