# Streamlit AI Assistant App
import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

# Set Streamlit page config
st.set_page_config(
    page_title="AI Assistant",
    page_icon=":robot_face:",
    layout="wide"
)

st.title("AI Assistant")
st.sidebar.title("Your AI Assistant")
st.sidebar.markdown("Chat with the AI Assistant.")

# Load environment variables once
load_dotenv()

# Initialize the model and agent once (cache for performance)
@st.cache_resource
def get_agent():
    model = ChatOpenAI(temperature=0, model="gpt-4o")
    tools = []
    return create_react_agent(model, tools)


agent_executor = get_agent()

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Assistant:** {msg['content']}")

# User input
user_input = st.text_input("You:", "", key="input")

if user_input:
    st.session_state["messages"].append({
        "role": "user",
        "content": user_input
    })
    response = ""
    with st.spinner("Assistant is typing..."):
        for chunk in agent_executor.stream({
            "messages": [HumanMessage(content=user_input)]
        }):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    response += message.content
                    # Show the response as it streams
                    st.markdown(f"**Assistant:** {response}")
    st.session_state["messages"].append({
        "role": "assistant",
        "content": response
    })
    st.stop()