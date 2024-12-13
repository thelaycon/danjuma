import os

from txtai import Embeddings
from ilimikudi.data import MoniepointBlogPosts

# Initialize embeddings
embeddings = Embeddings()

blog_posts = MoniepointBlogPosts()
data = blog_posts.get_data().to_dict('records')

# Prepare data for indexing
data_to_index = [(id, value["text"]) for id, value in enumerate(data)]

def embed(site: str, data: list) -> bool:
    # Create index if path does not exist
    if os.path.exists(f"{site}_index"):
        embeddings.load(f"{site}_index")
        return True
    else:
        print("Index not found. Now populating.")
        embeddings.index(data)
        embeddings.save(f"{site}_index")
        return True    



def index_data(site: str, data: list) -> None:
    # Calll embedding function
    response = embed(site, data)

    if response is True:
        print("Embedding loaded or created.")
    else:
        print("Failed to load or create embeddings.")


if __name__ == "__main__":
    index_data("moniepoint", data_to_index)