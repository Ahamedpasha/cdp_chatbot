import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def search_documentation(query, documentation_data):
    """
    Search through documentation data and return relevant results.
    :param query: The user query
    :param documentation_data: Dictionary of platform-specific tasks and details
    :return: A list of results or an empty list if no matches are found
    """
    try:
        results = []
        query_keywords = query.lower().split()  # Split the query into individual keywords
        
        for platform, tasks in documentation_data.items():
            for task, details in tasks.items():
                task_keywords = task.lower().split()  # Split task name into keywords
                description_keywords = details.lower().split()  # Split description into keywords

                # Check if any keyword in the query matches task or description keywords
                if any(keyword in task_keywords or keyword in description_keywords for keyword in query_keywords):
                    results.append((platform, task, details))
        
        return results
    except Exception as e:
        logging.error(f"Error occurred while searching documentation: {e}")
        return []
