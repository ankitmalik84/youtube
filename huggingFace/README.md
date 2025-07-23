# HuggingFace AI Image Generation Notebook

This Jupyter notebook demonstrates how to use HuggingFace's diffusion models for AI image generation, designed to work with Google Colab and various GPU configurations.

## 📋 Overview

This notebook provides a complete guide for:

- Setting up HuggingFace authentication
- Installing required dependencies for AI image generation
- Using Stable Diffusion models for text-to-image generation
- Running examples on both free T4 GPUs and more powerful hardware
- Generating high-quality AI images with customizable prompts

## 🚀 Features

- **Multi-GPU Support**: Works with both free T4 GPUs and premium GPU instances
- **HuggingFace Integration**: Seamless integration with HuggingFace model hub
- **Multiple Models**: Support for various diffusion models including Stable Diffusion Turbo
- **Easy Setup**: Step-by-step instructions for environment configuration
- **Example Prompts**: Pre-configured prompts for quick testing

## 🛠️ Prerequisites

- Google Colab account (recommended) or local Jupyter environment
- HuggingFace account (free)
- Basic understanding of Python and machine learning concepts

## 📦 Dependencies

The notebook automatically installs the following packages:

- `diffusers` - HuggingFace's diffusion models library
- `transformers` - Model architectures and tokenizers
- `accelerate` - Distributed training and inference
- `bitsandbytes` - Memory optimization
- `datasets` - Dataset handling utilities
- `fsspec` - File system interfaces

## 🔧 Setup Instructions

### 1. HuggingFace Authentication

Before running the notebook, you need to:

1. **Create a HuggingFace Account**:

   - Visit [https://huggingface.co](https://huggingface.co)
   - Sign up for a free account

2. **Generate API Token**:

   - Go to Settings → API Tokens
   - Create a new token with **WRITE** permissions (important!)

3. **Add Token to Colab**:
   - In Colab, click the key icon in the left sidebar
   - Add a new secret named `HF_TOKEN`
   - Paste your token as the value
   - Enable notebook access

### 2. Environment Setup

The notebook handles dependency installation automatically. Simply run the installation cells in order.

## 🎨 Usage Examples

### Basic Image Generation (Free T4 Compatible)

```python
from diffusers import AutoPipelineForText2Image
import torch

# Load the model
pipe = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/sd-turbo",
    torch_dtype=torch.float16,
    variant="fp16"
)
pipe.to("cuda")

# Generate an image
prompt = "A futuristic class full of students learning AI coding in a surreal style"
image = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]

# Display the result
image.show()
```

### Advanced Features

The notebook also includes examples for:

- Custom prompt engineering
- Model parameter tuning
- Batch image generation
- Memory optimization techniques

## 🖼️ Sample Prompts

Try these example prompts to get started:

- `"A futuristic class full of students learning AI coding in a surreal style"`
- `"A serene landscape with mountains and a crystal clear lake at sunset"`
- `"A cyberpunk cityscape with neon lights and flying cars"`
- `"An abstract digital art piece with vibrant colors and geometric shapes"`

## ⚡ Performance Tips

### For Free T4 GPUs:

- Use `sd-turbo` model for faster generation
- Set `num_inference_steps=1` for speed
- Use `torch.float16` for memory efficiency

### For Premium GPUs:

- Try more advanced models like Flux
- Increase inference steps for higher quality
- Experiment with different schedulers

## 🔍 Troubleshooting

### Common Issues:

1. **Authentication Errors**:

   - Ensure your HuggingFace token has WRITE permissions
   - Verify the token is correctly added to Colab secrets

2. **Memory Issues**:

   - Use smaller models on free GPUs
   - Enable memory optimization with `torch.float16`
   - Clear GPU memory between generations

3. **Model Loading Errors**:
   - Check internet connection
   - Verify model names are correct
   - Ensure sufficient disk space

## 📁 Notebook Structure

```
huggingFace.ipynb
├── Introduction & Setup
├── Package Installation
├── HuggingFace Authentication
├── Model Loading Examples
├── Image Generation (T4 Compatible)
```

## 🤝 Contributing

Feel free to:

- Add new model examples
- Improve prompt suggestions
- Optimize performance code
- Add error handling improvements

## 📜 License

This notebook is provided for educational purposes. Please respect:

- HuggingFace model licenses
- Google Colab usage policies
- Stable Diffusion licensing terms

## 🔗 Useful Links

- [HuggingFace Diffusers Documentation](https://huggingface.co/docs/diffusers/)
- [Stable Diffusion Model Card](https://huggingface.co/stabilityai/sd-turbo)
- [Google Colab Documentation](https://colab.research.google.com/)
- [Torch Documentation](https://pytorch.org/docs/)

## ⚠️ Important Notes

- **Model Usage**: Some models may have specific usage restrictions
- **Computational Resources**: Be mindful of Colab usage limits
- **Content Policy**: Follow ethical AI generation guidelines
- **Storage**: Generated images are temporary in Colab unless downloaded

---

Happy image generating! 🎨✨
