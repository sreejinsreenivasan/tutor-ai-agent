from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_community.tools import YouTubeSearchTool
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import streamlit as st

template= """You are a patient and insightful AI tutor tasked with helping students learn concepts through self-discovery and guided practice. 
Your role is to provide support, suggest relevant resources, and ensure the student is actively engaged in the learning process.

Answer the student questions. Suggest youtube videos to help them understand the concept better. 

Consider the student's current level of understanding based on their question. Identify any misconceptions or knowledge gaps that may need addressing.
Provide 1-2 targeted videos that are relevant to the question and can help build the necessary foundational knowledge.

Encourage the student to attempt the problem themselves first, using guiding questions or breaking it down into smaller steps if needed. Emphasize the importance of actively working through examples.
Outline a plan for how you will support the student if they struggle with the self-attempt, such as providing hints, asking probing questions, or working through the problem step-by-step.  

Remember, the goal is to foster an active learning mindset where the student develops a deeper conceptual understanding through exploration and your guidance. Be encouraging, adjust your approach based on their needs, and celebrate their efforts throughout the process.

{chat_history}
Human: {input}
Thought:{agent_scratchpad}
"""

tools = [YouTubeSearchTool()]

memory = ConversationBufferMemory(memory_key="chat_history",input_key="input")
prompt = PromptTemplate(
    input_variables=["chat_history", "input", ],
    template=template,
    tools=tools,
    tool_names=[tool.name for tool in tools],
)

# Choose the LLM that will drive the agent
llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.7)

# Construct the OpenAI Tools agent
agent = create_openai_tools_agent(llm, tools, prompt)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, memory=memory, max_iterations=10)

st.set_page_config(page_title="TutorAI", page_icon="🎓")
st.title("🎓 TutorAI: Your AI Learning Companion")

"""
TutorAI is an intelligent chatbot that adapts to your learning needs. Ask questions, receive explanations, get recommended resources, and practice with guidance. TutorAI fosters active learning through self-discovery and personalized support.

To get started, simply type your question or topic in the chat below.
"""

# Set up memory
msgs = StreamlitChatMessageHistory(key="langchain_messages")
if len(msgs.messages) == 0:
    msgs.add_ai_message("How can I help you?")

view_messages = st.expander("View the message contents in session state")

# Get an OpenAI API Key before continuing
if "openai_api_key" in st.secrets:
    openai_api_key = st.secrets.openai_api_key
else:
    openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Enter an OpenAI API Key to continue")
    st.stop()
    
# Render current messages from StreamlitChatMessageHistory
for msg in msgs.messages:
    st.chat_message(msg.type).write(msg.content)

# If user inputs a new prompt, generate and draw a new response
if input := st.chat_input():
    st.chat_message("human").write(input)
    # Note: new messages are saved to history automatically by Langchain during run

    response = agent_executor.invoke({"input": input})
    st.chat_message("ai").write(response["output"])

# Draw the messages at the end, so newly generated ones show up immediately
with view_messages:
    """
    Message History initialized with:
    ```python
    msgs = StreamlitChatMessageHistory(key="langchain_messages")
    ```

    Contents of `st.session_state.langchain_messages`:
    """
    view_messages.json(st.session_state.langchain_messages)