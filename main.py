import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from history.blog_context_toolcalls import moniepoint_few_shot_prompt
from tools.blog_context import get_context

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
    model=LLM_MODEL_NAME
)

# Bind tools to the language model
tools = [get_context]
llm_with_tools = llm.bind_tools(tools)

# Prepare the prompt
prompt = moniepoint_few_shot_prompt.invoke({"query": "Made wrong transfer"})
messages = prompt.to_messages()

# Fetch AI response
response = llm_with_tools.invoke(messages)
messages.append(response)

# Process tool calls and append responses
for tool_call in response.tool_calls:
    tool_message = get_context.invoke(tool_call)
    messages.append(tool_message)

# Print final AI response
final_response = llm.invoke(messages)
print(final_response)