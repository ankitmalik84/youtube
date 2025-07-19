from url_chat_processor import URLChatProcessor

def main():
    """
    Example usage of the URLChatProcessor class.
    """
    try:
        # Initialize the processor
        processor = URLChatProcessor()
        
        print("\n" + "="*50)
        print("🌊 Testing streaming response...")
        stream_result = processor.chat("https://personal-portfolio-gamma-red.vercel.app", max_results=1, stream=True)
        if stream_result['success']:
            analysis = stream_result['analyses'][0]
            print(f"🌍 {analysis['title']}")
            print(f"📝 Analysis: {analysis['analysis']}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Make sure you have set the required environment variables:")
        print("   - TAVILY_API_KEY")
        print("   - OPEN_ROUTER_KEY")

if __name__ == "__main__":
    main() 