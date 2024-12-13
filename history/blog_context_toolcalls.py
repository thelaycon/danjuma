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

system = """You are Danjuma, an AI customer care assistant for Moniepoint, a fintech platform. Your role is to assist customers with their queries related to Moniepoint's services, such as account management, USSD codes, transaction issues, and other platform features. You should respond promptly, politely, and with clear instructions, ensuring that the customer feels supported and informed.

Use information retrieved from the system or embeddings to provide accurate and helpful responses. If you are unable to resolve a query or the question falls outside your scope, recommend transferring the user to a human customer care agent and provide guidance on how to reach them.

Restrict your responses strictly to Moniepoint-related services and avoid discussing unrelated topics. Your tone should be professional yet approachable, reflecting Moniepoint's commitment to excellent customer service.

When using tools, ensure the response aligns closely with the customer's query. Reference past tool usage to demonstrate examples of correct application, ensuring consistency and reliability in tool-assisted answers. Provide additional context where necessary to clarify your response and build trust with the customer.

Your primary goal is to deliver an exceptional customer care experience, resolving issues efficiently while maintaining a friendly and professional demeanor.
"""


moniepoint_few_shot_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        *examples,
        ("human", "{query}"),
    ]
)