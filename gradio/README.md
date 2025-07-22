# FlightAI Chatbot

A multi-model chatbot interface built with Gradio that provides airline customer service assistance. The chatbot supports multiple AI models including OpenAI GPT-4o-mini and local models via Ollama.

## Features

- **Multi-Model Support**: Switch between different AI models via dropdown
  - OpenAI GPT-4o-mini
  - LLAMA3.2 (via Ollama)
  - DeepSeek-R1 1.5B (via Ollama)
- **Real-time Streaming**: Responses stream in real-time for better user experience
- **Airline-Focused**: Specialized system prompt for airline customer service
- **Modern UI**: Clean, responsive interface using Gradio's Soft theme
- **Jupyter Integration**: Runs seamlessly in Jupyter notebooks with embedded preview

## Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab
- OpenAI API key (for GPT-4o-mini)
- Ollama installed locally (for local models)

## Installation

1. **Clone or download the notebook** to your project directory

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install required packages**:

   ```bash
   pip install gradio openai python-dotenv requests jupyter ipywidgets
   ```

4. **Set up environment variables**:
   Create a `.env` file in your project root:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Install Ollama** (for local models):
   - Download from [https://ollama.ai](https://ollama.ai)
   - Install the required models:
     ```bash
     ollama pull llama3.2:1b
     ollama pull deepseek-r1:1.5b
     ```

## Usage

### Running the Notebook

1. **Start Jupyter**:

   ```bash
   jupyter notebook
   ```

2. **Open** `gradio.ipynb`

3. **Run all cells** or execute them step by step:
   - Cell 1: Import dependencies and load environment
   - Cell 2: Initialize OpenAI client
   - Cell 3: Set up system message
   - Cells 4-5: Simple chat interface (optional)
   - Cells 6-9: Advanced multi-model interface

### Using the Chatbot

1. **Select a model** from the dropdown menu
2. **Type your message** in the text input
3. **Press Enter** or click submit
4. **View the streaming response** in the chat interface

### Model Options

- **OpenAI GPT-4o-mini**: Requires API key, cloud-based, high quality
- **LLAMA3.2 (Ollama)**: Local model, faster inference, privacy-focused
- **DeepSeek-R1 1.5B (Ollama)**: Lightweight local model, good for basic queries

## Configuration

### System Message

The chatbot uses a specialized system prompt for airline customer service:

```python
system_message = "You are a helpful assistant for an Airline called FlightAI."
system_message += "Give Short, courteous answers. no more than 1 sentence."
system_message += "Always be accurate. If you don't know the answer, say so."
```

You can modify this in the notebook to customize the chatbot's behavior.

### Adding New Models

To add new models, update the `MODEL_OPTIONS` dictionary:

```python
MODEL_OPTIONS = {
    "Model Display Name": "provider:model_name",
    # Add your new model here
}
```

Supported providers:

- `openai`: For OpenAI models
- `ollama`: For local Ollama models

## Troubleshooting

### Common Issues

1. **OpenAI API Error**:

   - Verify your API key in the `.env` file
   - Check your OpenAI account has available credits

2. **Ollama Connection Error**:

   - Ensure Ollama is running: `ollama serve`
   - Verify models are installed: `ollama list`
   - Check Ollama is accessible at `http://localhost:11434`

3. **Import Errors**:

   - Install missing packages: `pip install [package-name]`
   - Verify virtual environment is activated

4. **Jupyter Widget Warning**:
   - Update Jupyter and ipywidgets: `pip install --upgrade jupyter ipywidgets`
   - Enable widgets: `jupyter nbextension enable --py widgetsnbextension`

### Performance Tips

- Use local models (Ollama) for faster response times
- Restart Ollama service if responses become slow
- Consider using smaller models for development and testing

## Project Structure

```
project/
├── gradio.ipynb          # Main notebook file
├── .env                  # Environment variables (create this)
├── README.md            # This file
```

## Dependencies

- `gradio`: Web interface framework
- `openai`: OpenAI API client
- `python-dotenv`: Environment variable management
- `requests`: HTTP requests for Ollama
- `jupyter`: Notebook environment
- `ipywidgets`: Interactive widgets

## Support

For issues and questions:

- Check the troubleshooting section above
- Review Gradio documentation: [https://gradio.app](https://gradio.app)
- OpenAI API documentation: [https://platform.openai.com/docs](https://platform.openai.com/docs)
- Ollama documentation: [https://ollama.ai/docs](https://ollama.ai/docs)
