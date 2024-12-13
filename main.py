import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from history.blog_context_toolcalls import moniepoint_few_shot_prompt
from tools.blog_context import get_context
from tools.assistant_context import answer_greeting

# Load environment variables
load_dotenv()

# Constants
LLM_API_KEY = os.environ["LLM_API_KEY"]
LLM_BASE_URL = "https://api.together.xyz/v1"
LLM_MODEL_NAME = "meta-llama/Llama-3.3-70B-Instruct-Turbo"

# Initialize the language model
llm = ChatOpenAI(
    base_url=LLM_BASE_URL,
    api_key=LLM_API_KEY,
    model=LLM_MODEL_NAME,
    max_retries=3,
    timeout=None
)

# Streamlit app setup
st.title("Danjuma")
st.write("Ask me anything about Moniepoint!")

# Initialize session state for messages and model
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input area
if prompt := st.chat_input("Type your message here..."):
    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare the prompt using moniepoint tool
    prepared_prompt = moniepoint_few_shot_prompt.invoke({"query": prompt})
    messages = prepared_prompt.to_messages()

    # Generate assistant response
    with st.chat_message("assistant"):
        stream = llm.stream(messages)
        response = st.write_stream(stream)
    # Append assistant's full response to session state
    st.session_state.messages.append({"role": "assistant", "content": response})
