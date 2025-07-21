# Company Brochure Generator

A Python-based tool that automatically generates engaging company brochures by analyzing their web presence. The tool uses both open source (Llama) and closed source (GPT) AI models to create informative and entertaining brochures suitable for prospective clients, investors, and potential recruits.

## Features

- 🌐 Automated web scraping of company websites
- 🔍 Intelligent link analysis and filtering
- 🤖 Dual AI model support:
  - Open source: Llama 3.2 (local inference)
  - Closed source: GPT-4o-mini (via OpenAI API)
- 📄 Markdown-formatted brochure output
- 😊 Humorous and engaging writing style

## Prerequisites

- Python 3.x
- OpenAI API key (for GPT model access)
- Ollama installed locally (for Llama model)
- Required Python packages (see requirements below)

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd brochure
```

2. Install Ollama (for Llama model):

```bash
# For macOS or Linux
curl -fsSL https://ollama.com/install.sh | sh

# For Windows
# Download from https://ollama.com/download
```

3. Pull the Llama model:

```bash
ollama pull llama3.2
```

4. Install required packages:

```bash
pip install -r requirements.txt
```

5. Set up your environment variables:

```bash
# Create a .env file and add your OpenAI API key
OPENAI_API_KEY=your-api-key-here
```

## Required Packages

```
requests
beautifulsoup4
python-dotenv
openai
ipython
jupyter
```

## Usage

The project is structured as a Jupyter notebook (`brochure.ipynb`) that demonstrates the brochure generation process:

1. Web scraping and content gathering
2. Intelligent link analysis
3. AI-powered brochure generation using either Llama or GPT models

### Model Configuration

The project supports two AI models:

1. **Llama 3.2 (Open Source)**

   - Runs locally through Ollama
   - No API costs
   - Suitable for development and testing

2. **GPT-4o-mini (Closed Source)**
   - Requires OpenAI API key
   - Pay-per-use pricing
   - Generally better quality output

You can switch between models by modifying the model parameter:

```python
# For Llama model
openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
MODEL = 'llama3.2'

# For GPT model
openai = OpenAI()
MODEL = 'gpt-4o-mini'
```

### Key Components

- `Website` class: Handles web scraping and content extraction
- `get_links()`: Analyzes and filters relevant website links
- `get_all_details()`: Gathers comprehensive information about the company
- `create_brochure()`: Generates the final brochure using the configured AI model

### Example Usage

```python
# Import required modules and set up environment
from dotenv import load_dotenv
load_dotenv()

# Configure the AI model
openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
MODEL = 'llama3.2'  # or 'gpt-4o-mini' for GPT model

# Create a brochure for a company
company_name = "Example Company"
website_url = "https://www.example.com"
create_brochure(company_name, website_url)
```

## Output

The tool generates a markdown-formatted brochure that includes:

- Company overview
- Culture insights
- Customer information
- Career opportunities
- Engaging and humorous content style

## Model Comparison

| Feature | Llama 3.2           | GPT-4o-mini      |
| ------- | ------------------- | ---------------- |
| Cost    | Free                | Pay per use      |
| Setup   | Local installation  | API key only     |
| Speed   | Depends on hardware | Consistent       |
| Quality | Good                | Very good        |
| Privacy | Data stays local    | Data sent to API |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT models
- Ollama team for the Llama model integration
- Beautiful Soup for web scraping capabilities
- All contributors and users of this project
