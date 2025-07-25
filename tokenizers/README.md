# Tokenizers: Understanding LLM Text Processing

This repository contains a comprehensive Jupyter notebook exploring **tokenizers** - a fundamental component of Large Language Models (LLMs) that converts human-readable text into numerical tokens that models can process.

## 🤖 What are Tokenizers?

Tokenizers are algorithms that break down text into smaller units called **tokens**. These tokens serve as the basic building blocks for language models to understand and process text. Think of tokenizers as translators that convert human language into a numerical format that neural networks can work with.

### Key Concepts:

- **Tokens**: Individual units of text (words, subwords, or characters) converted to numerical IDs
- **Vocabulary**: The complete set of tokens a model knows
- **Encoding**: Converting text → token IDs
- **Decoding**: Converting token IDs → text
- **Special Tokens**: Reserved tokens for specific purposes (start/end markers, padding, etc.)

## 📚 What This Notebook Covers

### 1. Basic Tokenization Operations

- **Text Encoding**: Converting sentences into numerical token arrays
- **Text Decoding**: Converting token arrays back to human-readable text
- **Individual Token Analysis**: Understanding how text gets split into tokens

### 2. Model-Specific Tokenizers

The notebook demonstrates tokenizers from multiple state-of-the-art models:

- **Meta Llama 3.1 8B**: Meta's latest instruction-tuned model
- **Microsoft Phi-3**: Compact yet powerful model
- **Qwen2**: Alibaba's multilingual model
- **StarCoder2**: Specialized for code generation

### 3. Advanced Features

#### Special Tokens

- Beginning/end of text markers (`<|begin_of_text|>`, `<|end_of_text|>`)
- Reserved tokens for future use
- Chat-specific tokens for conversation formatting

#### Chat Templates

- **Llama Format**: Uses header IDs for system/user/assistant roles
- **Qwen Format**: Uses `<|im_start|>` and `<|im_end|>` markers
- **Phi-3 Format**: Simplified system/user/assistant structure

#### Code Tokenization

- Specialized handling for programming languages
- Token-by-token breakdown of code syntax
- Understanding how models "see" source code

## 🔍 Key Insights from the Notebook

### Vocabulary Sizes

- **Llama 3.1**: 128,000 tokens (includes 256 special tokens)
- Different models have different vocabulary sizes optimized for their use cases

### Tokenization Differences

The same text: `"I am excited to show Tokenizers in action to my LLM engineers"`

Gets tokenized differently across models:

- **Llama**: 15 tokens (including special start token)
- **Phi-3**: 15 tokens
- **Qwen2**: 14 tokens
- **StarCoder2**: 16 tokens

### Chat Formatting

Each model uses different chat templates:

- **Llama**: Structured with headers and role IDs
- **Qwen**: Simple start/end markers
- **Phi-3**: Minimal formatting with pipe separators

## 🚀 Getting Started

### Prerequisites

```bash
pip install transformers huggingface_hub
```

### HuggingFace Authentication

The notebook requires a HuggingFace token for accessing some models:

1. Create an account at [HuggingFace](https://huggingface.co)
2. Generate an access token
3. Add it to your environment or Colab secrets

### Running the Notebook

1. Open `tokenizers.ipynb` in Jupyter/Colab
2. Install required dependencies
3. Set up HuggingFace authentication
4. Run cells sequentially to explore tokenization

## 💡 Why Tokenizers Matter

Understanding tokenizers is crucial for:

1. **Prompt Engineering**: Knowing how your text gets tokenized helps craft better prompts
2. **Model Selection**: Different tokenizers suit different tasks (code vs. chat vs. multilingual)
3. **Cost Optimization**: Token count directly impacts API costs and processing time
4. **Debugging**: Understanding tokenization helps diagnose model behavior
5. **Fine-tuning**: Custom tokenizers may be needed for specialized domains

## 🔬 Practical Applications

- **Token Counting**: Estimate API costs and context window usage
- **Cross-Model Comparison**: Understand efficiency differences between models
- **Chat Interface Development**: Implement proper conversation formatting
- **Code Generation**: Optimize prompts for programming tasks
- **Multilingual Processing**: Compare tokenization across languages
