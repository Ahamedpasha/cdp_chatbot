import time
import logging
from chatbot.search import search_documentation
from chatbot.config import load_config # type: ignore

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Chatbot:
    def __init__(self, config):
        """
        Initialize the chatbot with configuration data.
        :param config: Configuration data for platforms and tasks
        """
        self.documentation_data = config["documentation_data"]
    
    def display_results(self, results):
        """
        Display the search results to the user.
        :param results: The list of matched results
        """
        if results:
            print("\nHere are the relevant results:\n")
            for platform, task, details in results:
                print(f"[{platform}] {task}: {details}\n")
        else:
            print("Sorry, I couldn't find any relevant information. Try rephrasing your question.\n")
    
    def handle_query(self, query):
        """
        Handle the user's query and search for relevant documentation.
        :param query: The user's query
        """
        print("\nProcessing your request...")
        time.sleep(1)  # Simulate some thinking time
        
        results = search_documentation(query, self.documentation_data)
        self.display_results(results)
    
    def start_chat(self):
        """
        Start the chatbot interaction with the user.
        """
        print("Welcome to the CDP Chatbot!")
        print("You can ask 'How-to' questions related to Segment, mParticle, Lytics, and Zeotap.")
        print("Type 'exit' to quit anytime.\n")
        
        while True:
            user_query = input("You: ").strip()
            if user_query.lower() == "exit":
                print("Goodbye!")
                break
            
            self.handle_query(user_query)
