# URL Chat Processor 🚀

A Python tool that leverages the Tavily Search API to fetch web page content and uses a Large Language Model (LLM) via OpenRouter to generate comprehensive summaries.

This script can take a URL or a general search query, find relevant online content, and provide an individual AI-powered analysis for each result found.

---

## Features

- **Web Content Fetching**: Uses Tavily to perform a web search and retrieve the full content of target pages.
- **LLM Integration**: Connects to any LLM on the OpenRouter platform (defaults to the free `moonshotai/kimi-k2:free` model).
- **Dynamic Prompting**: Automatically creates detailed prompts for the LLM based on the fetched website data.
- **Structured Output**: Returns a clean, dictionary-formatted analysis for easy integration into other applications.
- **Configurable**: Easily change the target model, number of search results to analyze, and API keys.
- **Streaming Support**: Supports streaming responses from the LLM for real-time output.

---

## How It Works

The process follows a simple pipeline:

1.  **Input**: You provide a URL or a search query (e.g., `"https://example.com"` or `"latest advancements in AI"`).
2.  **Search**: The `TavilyClient` searches the web for the query and retrieves the content of the top matching pages.
3.  **Prompt Generation**: For each web page result, a detailed prompt is constructed, containing its title, URL, and full content.
4.  **AI Analysis**: This prompt is sent to an LLM via the OpenRouter API. The LLM analyzes the content and generates a summary based on a system prompt that guides it to focus on key information.
5.  **Output**: The script collects the analysis for each processed URL and returns a single JSON object containing all the summaries.

---

## ⚙️ Setup and Installation

### 1. Clone the Repository

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Create a `requirements.txt` file with the following content:

```
openai
python-dotenv
tavily-python
```

Then, install them using pip:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

You need API keys for Tavily and OpenRouter.

Create a file named `.env` in the root of your project directory and add your keys:

```
TAVILY_API_KEY="your_tavily_api_key_here"
OPEN_ROUTER_KEY="your_openrouter_api_key_here"
```

> **Note**: You can get your keys from [Tavily AI](https://tavily.com/) and [OpenRouter.ai](https://openrouter.ai/).

---

## 💡 Usage

Here's a basic example of how to use the `URLChatProcessor` class. Create a file like `main.py` and add the following code:

```python
import json
from url_chat_processor import URLChatProcessor # Assuming your class is in this file

# 1. Initialize the processor
# It will automatically load keys from your .env file
processor = URLChatProcessor()

# 2. Define a URL or search query to analyze
# url_to_check = "[https://www.tavily.com/documentation](https://www.tavily.com/documentation)"
search_query = "What is Retrieval-Augmented Generation?"

# 3. Run the chat method
# You can change the model, number of results, and streaming option
analysis_result = processor.chat(
    url_or_query=search_query,
    max_results=2, # Analyze the top 2 search results
    model="google/gemini-flash-1.5", # Use a different model
    stream=False
)

# 4. Print the result in a readable format
print(json.dumps(analysis_result, indent=4))
```

### Example Output

The script will return a dictionary similar to this:

```json
{
  "success": true,
  "query": "What is Retrieval-Augmented Generation?",
  "total_results": 2,
  "analyses": [
    {
      "result_index": 0,
      "title": "What is retrieval-augmented generation? | TechTarget",
      "url": "[https://www.techtarget.com/whatis/definition/retrieval-augmented-generation-RAG](https://www.techtarget.com/whatis/definition/retrieval-augmented-generation-RAG)",
      "score": 0.9855,
      "analysis": "## Website Summary: TechTarget on RAG\n\n### 1. Main Topic/Purpose\nThe main purpose of this webpage is to provide a comprehensive definition and explanation of Retrieval-Augmented Generation (RAG). It targets an audience interested in AI and natural language processing, explaining what RAG is, how it works, and why it is important for improving large language models (LLMs).\n\n### 2. Key Information or Highlights\n- **Definition**: RAG is an AI technique that enhances LLMs by grounding them in external, authoritative knowledge bases.\n- **Functionality**: It works by retrieving relevant information (like documents or passages) from a data source and providing it to the LLM as context when generating a response.\n- **Benefits**: RAG helps to reduce hallucinations (incorrect or fabricated information), allows for more current and domain-specific responses, and provides source attribution for better trust and verification.\n\n### 3. Important Announcements or News\nThere are no specific announcements or time-sensitive news present on this page. It serves as an evergreen educational resource.\n\n### 4. Overall Assessment\nThe content is well-structured, clear, and highly informative. It effectively breaks down a complex technical topic for a professional audience, making it an excellent resource for anyone looking to understand RAG."
    },
    {
      "result_index": 1,
      "title": "What Is Retrieval-Augmented Generation (RAG)? - NVIDIA Blogs",
      "url": "[https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)",
      "score": 0.9742,
      "analysis": "## Website Summary: NVIDIA on RAG\n\n### 1. Main Topic/Purpose\nThis NVIDIA blog post explains Retrieval-Augmented Generation (RAG) from a more technical and industry-focused perspective. It aims to inform developers and businesses about the value of RAG in building enterprise-grade AI applications.\n\n### 2. Key Information or Highlights\n- **Enterprise Focus**: The article highlights RAG as a key component for building chatbots, question-answering systems, and other generative AI applications that rely on custom or proprietary data.\n- **Technical Workflow**: It describes the two main phases of RAG: the indexing phase (preparing the knowledge base) and the retrieval/generation phase (runtime).\n- **NVIDIA's Role**: The post mentions NVIDIA's tools and frameworks, like NeMo, that can be used to build and deploy RAG-based solutions.\n\n### 3. Important Announcements or News\nNo major news, but the content implicitly promotes NVIDIA's ecosystem for AI development.\n\n### 4. Overall Assessment\nThe content is authoritative and provides a practical perspective on implementing RAG. It is slightly more technical than the TechTarget article and serves as a great resource for developers looking to apply the technology."
    }
  ]
}
```
