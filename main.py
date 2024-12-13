import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_core.tools import tool

from dotenv import load_dotenv

from tools.blog_context import get_context

tools = [get_context]


load_dotenv()

LLM_API_KEY = os.environ["LLM_API_KEY"]

llm = ChatOpenAI(
    base_url = "https://api.together.xyz/v1",
    api_key = LLM_API_KEY,
    model = "meta-llama/Llama-3.3-70B-Instruct-Turbo"
)