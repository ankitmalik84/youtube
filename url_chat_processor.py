import os
from dotenv import load_dotenv
from tavily import TavilyClient
from openai import OpenAI
from typing import Dict, List, Optional

class URLChatProcessor:
    """
    A class that processes URLs by fetching content via Tavily search
    and then analyzing it with an LLM to provide summaries.
    """
    
    def __init__(self, tavily_api_key: Optional[str] = None, openrouter_api_key: Optional[str] = None):
        """
        Initialize the URL Chat Processor.
        
        Args:
            tavily_api_key: Tavily API key (if not provided, will try to get from env)
            openrouter_api_key: OpenRouter API key (if not provided, will try to get from env)
        """
        load_dotenv()
        
        # Initialize Tavily client
        self.tavily_api_key = tavily_api_key or os.getenv("TAVILY_API_KEY")
        if not self.tavily_api_key:
            raise ValueError("Tavily API key is required. Set TAVILY_API_KEY environment variable or pass it as parameter.")
        
        self.tavily_client = TavilyClient(self.tavily_api_key)
        
        # Initialize OpenAI client for OpenRouter
        self.openrouter_api_key = openrouter_api_key or os.getenv("OPEN_ROUTER_KEY")
        if not self.openrouter_api_key:
            raise ValueError("OpenRouter API key is required. Set OPEN_ROUTER_KEY environment variable or pass it as parameter.")
        
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.openrouter_api_key,
        )
        
        # Default system prompt
        self.system_prompt = """You are an assistant that analyzes the contents of a website 
and provides a comprehensive summary. Focus on the main content and ignore navigation elements.
Respond in markdown format with clear sections."""

    def search_url_content(self, query: str, max_results: int = 5) -> List[Dict]:
        """
        Search for content related to the query using Tavily.
        
        Args:
            query: Search query
            max_results: Maximum number of results to return
            
        Returns:
            List of search results
        """
        try:
            response = self.tavily_client.search(query)
            results = response.get("results", [])
            return results[:max_results]
        except Exception as e:
            print(f"Error searching with Tavily: {e}")
            return []

    def create_user_prompt(self, website_data: Dict) -> str:
        """
        Create a user prompt for the LLM based on website data.
        
        Args:
            website_data: Dictionary containing website information
            
        Returns:
            Formatted user prompt
        """
        title = website_data.get("title", "Unknown Title")
        content = website_data.get("content", "")
        url = website_data.get("url", "")
        
        user_prompt = f"""You are analyzing a website with the following information:

Title: {title}
URL: {url}

Content:
{content}

Please provide a comprehensive summary of this website in markdown format. Include:
1. Main topic/purpose of the website
2. Key information or highlights
3. Any important announcements or news if present
4. Overall assessment of the content

Format your response in clear markdown sections."""
        
        return user_prompt

    def chat_with_llm(self, user_prompt: str, model: str = "moonshotai/kimi-k2:free", 
                      stream: bool = False) -> str:
        """
        Send a prompt to the LLM and get a response.
        
        Args:
            user_prompt: The user prompt to send
            model: The model to use
            stream: Whether to stream the response
            
        Returns:
            LLM response as string
        """
        try:
            completion = self.client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "https://github.com/your-repo",
                    "X-Title": "URL Chat Processor",
                },
                model=model,
                stream=stream,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )
            
            if stream:
                response_text = ""
                for chunk in completion:
                    if chunk.choices[0].delta.content:
                        response_text += chunk.choices[0].delta.content
                return response_text
            else:
                return completion.choices[0].message.content
                
        except Exception as e:
            print(f"Error communicating with LLM: {e}")
            return f"Error: {str(e)}"

    def chat(self, url_or_query: str, max_results: int = 3, 
             model: str = "moonshotai/kimi-k2:free", stream: bool = False) -> Dict:
        """
        Main chat method that processes a URL or query and returns analysis.
        
        Args:
            url_or_query: URL or search query to analyze
            max_results: Maximum number of search results to process
            model: LLM model to use
            stream: Whether to stream LLM responses
            
        Returns:
            Dictionary containing analysis results
        """
        # Search for content related to the URL/query
        search_results = self.search_url_content(url_or_query, max_results)
        
        if not search_results:
            return {
                "success": False,
                "error": "No search results found",
                "query": url_or_query
            }
        
        # Process each result with LLM
        analyses = []
        for i, result in enumerate(search_results):
            user_prompt = self.create_user_prompt(result)
            llm_response = self.chat_with_llm(user_prompt, model, stream)
            
            analyses.append({
                "result_index": i,
                "title": result.get("title", "Unknown"),
                "url": result.get("url", ""),
                "score": result.get("score", 0),
                "analysis": llm_response
            })
        
        return {
            "success": True,
            "query": url_or_query,
            "total_results": len(search_results),
            "analyses": analyses
        }