from pydantic import BaseModel, Field
from langchain_core.tools import tool


class AboutAssistantInput(BaseModel):
    """
    Schema for input arguments to the get_about_assistant tool.
    """
    greeting: str = Field(
        default="Hello",
        description="Greeting from the user or question about the assistant's capabilities or role."
    )


@tool
def answer_greeting(greeting: str, args_schema=AboutAssistantInput, return_direct=True) -> str:
    """

    Answers users greeting like Good morning, Hi, Hello, and the likes.

    Args:
        query (str): The user's greeting or question about the assistant.
        args_schema (type): Validation schema for input arguments.
        return_direct (bool): Flag to indicate whether to return the result directly.

    Returns:
        str: The static information about the assistant in string form.
    """
    # Static information about the assistant as a string
    assistant_info = (
        f"Use the information below to respond to the greeting: '{greeting}'"
        "I am Danjuma, an AI assistant for Moniepoint. "
        "My role is to assist you with your queries regarding Moniepoint's services, "
        "such as account management, USSD codes, transaction issues, and other platform features. "
        "I can help you check your account balance, reset your PIN, provide USSD codes for services, "
        "and much more. If I can't resolve your query, I will guide you to a human customer care agent. "
        "You can ask me anything related to Moniepoint, and I will do my best to assist you."
        "Give short response"
    )

    # Return the assistant information as a string
    return assistant_info.replace("\n", "")
