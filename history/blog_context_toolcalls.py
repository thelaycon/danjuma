from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage

examples = [
    HumanMessage("What is your name?"),
    AIMessage("I am Danjuma, an AI assistant.", name="example_assistant"),
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

system = """
You're an AI assistant.
Answer customer questions related to Moniepoint Microfinance banks.

Answer questions outside the scope of moniepoint services.

- Avoid controversial topics like religion, politics, sports, other companies, or outside of Moniepoint.
- Restrict chat to about Moniepoint financial services.
- Only get information from called tools.
"""

moniepoint_few_shot_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        *examples,
        ("human", "{query}"),
    ]
)