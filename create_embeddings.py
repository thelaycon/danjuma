import os
from typing import List
from pydantic import BaseModel, ValidationError
from txtai import Embeddings
from ilimikudi.data import MoniepointBlogPosts

# Initialize embeddings with default model
embeddings = Embeddings()

# Define Pydantic model for data validation
class BlogPost(BaseModel):
    id: str
    text: str

# Load data
blog_posts = MoniepointBlogPosts()
data = blog_posts.get_data().to_dict('records')

# Validate data with Pydantic
def validate_data(data: List[dict]) -> List[BlogPost]:
    """
    Validates data using the BlogPost Pydantic model.
    Args:
        data (List[dict]): Raw data to validate.
    Returns:
        List[BlogPost]: A list of validated BlogPost objects.
    Raises:
        ValidationError: If any data item fails validation.
    """
    validated_data = []
    for idx, record in enumerate(data):
        try:
            validated_data.append(BlogPost(id=str(idx), text=record["text"]))
        except ValidationError as e:
            print(f"Validation error for record {idx}: {e}")
    return validated_data

# Prepare and validate data
validated_data = validate_data(data)
data_to_index = [(item.id, item.text) for item in validated_data]

def embed(site: str, data: list) -> bool:
    """
    Embed and save data to an index.
    Args:
        site (str): Name of the site, used as part of the index path.
        data (list): Data to index as a list of tuples (id, text).
    Returns:
        bool: True if embedding is created or loaded successfully, False otherwise.
    """
    index_path = f"{site}_index"
    if os.path.exists(index_path):
        embeddings.load(index_path)
        print(f"Index loaded from {index_path}.")
        return True
    else:
        print("Index not found. Now populating.")
        embeddings.index(data)
        embeddings.save(index_path)
        print(f"Index created and saved at {index_path}.")
        return True    

def index_data(site: str, data: list) -> Embeddings:
    """
    Indexes data for a given site and returns the embeddings.
    Args:
        site (str): Name of the site.
        data (list): List of data tuples (id, text).
    Returns:
        Embeddings: The embeddings object after indexing or loading.
    """
    response = embed(site, data)
    if response:
        print("Embedding loaded or created.")
        return embeddings
    else:
        print("Failed to load or create embeddings.")
        return None

# Index data
embedding_model = index_data("moniepoint", data_to_index)