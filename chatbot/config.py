import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file="chatbot/config.json"):
    """
    Load the configuration data from a JSON file.
    :param config_file: Path to the config file
    :return: Parsed JSON data as a dictionary
    """
    try:
        with open(config_file, "r") as f:
            config = json.load(f)
            return config
    except Exception as e:
        logging.error(f"Error loading config file {config_file}: {e}")
        return {}
