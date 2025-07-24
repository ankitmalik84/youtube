# HuggingFace Pipelines Tutorial

A comprehensive Jupyter notebook demonstrating the power and simplicity of HuggingFace Transformers library's high-level pipeline API for various Natural Language Processing (NLP) tasks.

## 📖 Overview

This notebook serves as a complete guide to the HuggingFace Pipelines API, showcasing how to perform complex NLP tasks with minimal code. The pipeline API provides a high-level interface for **inference** (running pre-trained models) without requiring deep knowledge of the underlying model architectures.

## 🎯 Key Concepts Covered

### Training vs Inference

- **Training**: Adapting models by updating parameters/weights with data
- **Inference**: Using pre-trained models to generate outputs on new inputs
- This notebook focuses exclusively on **inference** using pre-trained models

## 🚀 Features Demonstrated

### 1. **Sentiment Analysis**

```python
classifier = pipeline("sentiment-analysis")
result = classifier("I'm super excited to be on the way of LLM mastery")
```

- Determines emotional tone of text (positive/negative)
- Uses DistilBERT model by default

### 2. **Named Entity Recognition (NER)**

```python
ner = pipeline("ner", grouped_entities=True)
result = ner("Barack Obama was the 44th president of the United States")
```

- Identifies and classifies named entities (persons, locations, organizations)
- Groups related tokens for better results

### 3. **Question Answering**

```python
question_answering = pipeline("question-answering")
result = question_answering(
    question="Who was the 44th president of the United States?",
    context="Barack Obama was the 44th president of the United States"
)
```

- Extracts answers from provided context
- Returns confidence scores with answers

### 4. **Text Summarization**

```python
summarizer = pipeline("summarization")
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
```

- Condenses long text into shorter summaries
- Configurable length parameters

### 5. **Translation**

```python
# English to French
translator = pipeline("translation_en_to_fr")

# English to Spanish with specific model
translator = pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es")
```

- Supports multiple language pairs
- Option to specify custom translation models

### 6. **Zero-Shot Classification**

```python
classifier = pipeline("zero-shot-classification")
result = classifier(
    "Hugging Face's Transformers library is amazing",
    candidate_labels=["technology", "sports", "politics"]
)
```

- Classifies text without training on specific categories
- Provides confidence scores for each candidate label

### 7. **Text Generation**

```python
generator = pipeline("text-generation")
result = generator("If there's one thing I want you to remember about using Hugging Face pipelines, it's")
```

- Continues text based on initial prompt
- Uses GPT-2 model by default

### 8. **Text-to-Speech**

```python
synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")
speech = synthesiser("Hi to an artificial Intelligence engineer, on the way to mastery!")
```

- Converts text to audio speech
- Supports speaker embeddings for voice customization

## 🛠️ Setup & Requirements

### Environment

- **Platform**: Google Colab (with GPU support)
- **Python**: 3.11+
- **CUDA**: 12.4 support

### Dependencies

```bash
# Core packages
torch==2.5.1+cu124
torchvision==0.20.1+cu124
torchaudio==2.5.1+cu124
transformers==4.48.3
datasets==3.2.0
diffusers
soundfile
```

### Installation

The notebook includes automatic installation commands:

```python
!pip install -q --upgrade torch==2.5.1+cu124 torchvision==0.20.1+cu124 torchaudio==2.5.1+cu124 --index-url https://download.pytorch.org/whl/cu124
!pip install -q --upgrade transformers==4.48.3 datasets==3.2.0 diffusers
```

## 🔑 Authentication

The notebook requires HuggingFace authentication:

```python
from huggingface_hub import login
from google.colab import userdata

hf_token = userdata.get('HF_TOKEN')
login(hf_token, add_to_git_credential=True)
```

**Setup Instructions:**

1. Create a HuggingFace account at [huggingface.co](https://huggingface.co)
2. Generate an access token in your HF settings
3. Add the token to Google Colab secrets as `HF_TOKEN`

## 💡 Key Advantages of Pipelines API

1. **Simplicity**: Complex NLP tasks in just 2-3 lines of code
2. **Consistency**: Uniform interface across different tasks
3. **Flexibility**: Easy model swapping and customization
4. **GPU Support**: Automatic device management with `device="cuda"`
5. **Production Ready**: Built-in optimizations for inference

## 📝 Usage Examples

### Basic Pattern

```python
# 1. Create pipeline
my_pipeline = pipeline("task_name", device="cuda")

# 2. Use pipeline
result = my_pipeline(input_text)

# 3. Process results
print(result)
```

### Advanced Usage

```python
# Custom model specification
translator = pipeline("translation_en_to_es",
                     model="Helsinki-NLP/opus-mt-en-es",
                     device="cuda")

# Parameter customization
summarizer = pipeline("summarization", device="cuda")
summary = summarizer(text,
                    max_length=50,
                    min_length=25,
                    do_sample=False)
```

## 🎯 Learning Outcomes

After completing this notebook, you will:

- Understand the difference between training and inference
- Master the HuggingFace Pipelines API syntax
- Know how to perform 8+ different NLP tasks
- Be able to customize models and parameters
- Understand GPU acceleration setup
- Have hands-on experience with state-of-the-art NLP models

## 📚 Next Steps

This notebook covers the **high-level** Pipelines API. For more advanced usage:

- Explore lower-level HuggingFace Transformers APIs
- Learn about model fine-tuning
- Study custom model training
- Dive into specific model architectures

---

**Happy Learning! 🚀**
