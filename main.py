import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_core.tools import tool

from dotenv import load_dotenv

load_dotenv()

LLM_API_KEY = os.environ["LLM_API_KEY"]

llm = ChatOpenAI(
    base_url = "https://api.together.xyz/v1",
    api_key = LLM_API_KEY,
    model = "mistralai/Mixtral-8x7B-Instruct-v0.1"
)

messages = [
    SystemMessage(content="I am a banking customer care"),
    HumanMessage(content="Hello there, how are you?")
]

response = llm.invoke(messages)

print(response)