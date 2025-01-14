from chatbot.chatbot import Chatbot
from chatbot.config import load_config # type: ignore

def main():
    # Load configuration
    config = load_config()

    if config:
        chatbot = Chatbot(config)
        chatbot.start_chat()
    else:
        print("Failed to load configuration. Exiting.")

if __name__ == "__main__":
    main()