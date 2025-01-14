# cdp_chatbot

Description:
In this project, a "How-to" chatbot is deployed that assists a user in identifying answers related to tasks and feature capabilities of four Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. Information relevant to questions asked by a user is sourced from preconfigured documentation and furnished to the users in a chat-like interface.

Features
• Answer "How-to" Questions: The four platforms mentioned will be able to answer questions with regard to setup sources, event tracking, creating segments, among others.
- Documentation Search: It pulls information from pre-set documentation and sends the related steps to the user.
- Cross-Platform Compatibility: It supports all four platforms—Segment, mParticle, Lytics, and Zeotap.
- User Interaction: The chatbot communicates with the users through the command-line interface.

Folder Structure:
-----------------
cdp_chatbot/
│
├── chatbot/
│   ├── __init__.py        # Makes the directory a Python package
│   ├── chatbot.py         # Main chatbot logic
│   ├── search.py          # Search functionality
│   └── config.json        # Platform-specific configuration and tasks
│
├── tests/
│   └── test_chatbot.py    # Unit tests for chatbot functionality
│
├── main.py             # Main entry point for running the chatbot
 └── requirements.txt    # Project dependencies (empty for now)

Prerequisites:
----------------
- Python 3.x
- Make sure you have the required Python modules installed. Refer to the requirements.txt file for details.

Setup:
------
1. Install dependencies:
This project doesn't have any external dependencies as of now. If you plan to add some later, add them to requirements.txt.

2. Configure documentation data:
    - Edit chatbot/config.json so that it has the proper documentation data about the platforms
    - Refer to the template of config.json in the project.

   Example config.json:
{
     "documentation_data": {
       "Segment": {
         "Set up a new source": "Go to your workspace, click 'Add Source', and choose your integration.",
         "Track events": "Use Segment's tracking library to record user events."
       },
"mParticle": Explore
        "Create a user profile": Go to the Users section, click 'Create Profile', and fill in the details.
        "Set up an event integration": Go to Integrations, choose your destination, and configure events.
"Lytics": 
         "Build an audience segment": "In Lytics, go to the Audience tab, select 'Create Segment', and apply your filters.",
         "View user data": "Access user profiles by navigating to the Data tab.
"Zeotap": {
         "Integrate data": "Visit the Integration section, select your source, and follow the guided steps.",
         "Export audience segments": "Go to the Audience section, click 'Export', and choose the desired format."
       }
     }
   }

3. Run the chatbot:
   Once you have finished the setup, you can run the chatbot by running the main.py file.

   python main.py

   You will be prompted to type in your queries. For example:

   - "How do I set up a new source in Segment?"
   - "How can I create a user profile in mParticle?"
Type in `exit` to exit the chatbot.
