# TutorAI: Your AI Learning Companion

## Project Description

TutorAI is an AI-powered chatbot designed to support your learning journey. By fostering an active learning environment, TutorAI encourages self-discovery through:

- Personalized explanations: Ask questions about various topics and receive clear and concise explanations tailored to your needs.
- Recommended resources: Get directed to relevant resources like YouTube videos that supplement your learning and solidify understanding.
- Guided practice: Practice your newfound knowledge with guidance from TutorAI. This can involve hints, step-by-step breakdowns, and encouraging messages.

## Getting Started

### Prerequisites:

- An OpenAI API Key (obtainable from [OpenAI API](https://beta.openai.com/account/api-keys))
- Python environment with required libraries (instructions below)

### Installation:

1. Clone this repository.
2. Create a virtual environment (recommended) and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the application:

- Set your OpenAI API Key as a secret in Streamlit:

  ```python
  st.secrets["openai_api_key"] = "<YOUR_OPENAI_API_KEY>"
  ```

- Run the application from the project directory:

  ```bash
  streamlit run main.py
  ```

## User Interface

The user interface features a chat-based interaction. Simply type your question or topic in the chat box at the bottom of the page. TutorAI will analyze your input and provide a response that may include:

- A clear explanation of the concept
- Recommended YouTube videos for further learning
- Guidance on how to approach a problem or practice your understanding

The conversation history is displayed on the screen, allowing you to revisit previous interactions.

## Implementation Details

This project utilizes several libraries to achieve its functionality:

- Langchain: A framework for building interactive AI systems.
- Streamlit: A web framework for building data apps in Python.
- ChatOpenAI: A Langchain wrapper for OpenAI's GPT-3 language model.
- YouTubeSearchTool: A Langchain tool for searching YouTube videos.
- StreamlitChatMessageHistory: A custom component for managing chat history in Streamlit.

The core logic utilizes a ReAct prompt format guiding the AI model's interaction with the user. This involves analyzing the user's question, suggesting relevant resources, encouraging self-discovery, and offering support when needed. Finally, the model assesses the user's comprehension and recommends further learning paths.

## Additional Notes

- This project serves as a foundation for building a more robust AI tutor.
- You can explore customizing the prompt template for more specific subject areas or learning styles.
- Consider integrating additional resources beyond YouTube videos, such as articles or interactive exercises.
- For production deployment, consider security measures for handling user input and API keys.

We hope TutorAI empowers you on your learning journey!
