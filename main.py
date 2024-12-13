import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage

from langchain_core.runnables import RunnablePassthrough

from dotenv import load_dotenv

from history.blog_context_toolcalls import moniepoint_few_shot_prompt
from tools.blog_context import get_context

tools = [get_context,]


load_dotenv()

LLM_API_KEY = os.environ["LLM_API_KEY"]

llm = ChatOpenAI(
    base_url = "https://api.together.xyz/v1",
    api_key = LLM_API_KEY,
    model = "meta-llama/Llama-3.3-70B-Instruct-Turbo"
)

llm_with_tools = llm.bind_tools(tools)

chain = {"query": RunnablePassthrough()} | moniepoint_few_shot_prompt | llm_with_tools
print(chain.invoke("What's moniepont ussd").tool_calls)