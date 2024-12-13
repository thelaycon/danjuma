from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage

examples = [
    HumanMessage("What is the Moniepoint USSD code?", name="example_user"),
    AIMessage(
        "",
        name="example_assistant",
        tool_calls=[
            {
                "name": "get_context",
                "args": {
                    "query": "Moniepoint USSD code",
                },
                "id": "1",
            }
        ],
    ),
    ToolMessage("The Moniepoint USSD code is *5573# for accessing services.", tool_call_id="1"),
    AIMessage(
        "",
        name="example_assistant",
        tool_calls=[
            {
                "name": "get_context",
                "args": {
                    "query": "Check Moniepoint account balance",
                },
                "id": "2"            }
        ],
    ),
    ToolMessage("You can check your account balance by using the mobile app or using the ussd.", tool_call_id="2"),
    AIMessage(
        "",
        name="example_assistant",
        tool_calls=[
            {
                "name": "get_context",
                "args": {
                    "query": "Forgot Moniepoint PIN",
                },
                "id": "3",
            }
        ],
    ),
    ToolMessage(
        "If you forget your PIN, reset it by using the mobile app and following the prompts.",
        tool_call_id="3"
    ),
    AIMessage("Use the mobile app to reset your pin.", name="example_assistant"),
]

system = """You are an AI customer care assistant for Moniepoint. Answer customer queries using information retrieved from the system or embeddings.
When using tools, ensure the response aligns closely with the customer's query.

Always use the  past tool usage as an example of how to correctly use the tools. 
"""

moniepoint_few_shot_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        *examples,
        ("human", "{query}"),
    ]
)