from pydantic import BaseModel, Field
from langchain_core.tools import tool
from create_embeddings import embedding_model, data


class Query(BaseModel):
    """
    Schema to validate the query input for searching embeddings.
    """
    query: str


def search_embeddings(query: str) -> str:
    """
    Searches the embeddings for the most relevant result.

    Args:
        query (str): The query string to search for.

    Returns:
        str: The corresponding text from the data for the best match.
    """
    # Validate the query input
    query_model = Query(query=query)

    # Perform the search and retrieve the top match
    matched_id = embedding_model.search(query_model.query, 1)[0][0]

    # Return the associated text
    return data[matched_id]


class ContextInput(BaseModel):
    """
    Schema for input arguments to the get_context tool.
    """
    query: str = Field(
        default="Hello Danjuma", 
        description="Query or question to be searched in the embeddings or database."
    )


@tool
def get_context(query: str, args_schema=ContextInput, return_direct=True) -> str:
    """
    Extracts relevant information from the embeddings to answer the user's query.

    Args:
        query (str): The user's query or question.
        args_schema (type): Validation schema for input arguments.
        return_direct (bool): Flag to indicate whether to return the result directly.

    Returns:
        str: The text context corresponding to the user's query.
    """
    # Search for relevant context based on the query
    result_text = search_embeddings(query)

    prompt_result = f"""
            Answer the question '{query}' using the information below:

            context: {result_text}

            Be helpful and kind. Attempt to answer the question. Response should be detailed and contain the following:
            - The issue at hand.
            - Why that could happen.
            - How to resolve (use context given above)
            - Next steps.

            Note, you're a Moniepoint support. Don't refer them to a human agent without helping first.

            General support details:

            Calling +234 201 888 9990 
            Emailing support@moniepoint.com
    """
    return prompt_result