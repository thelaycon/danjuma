# Danjuma

## Overview
Danjuma is an AI-powered assistant designed to help users with queries related to Moniepoint's services. It utilizes state-of-the-art AI technologies and Retrieval-Augmented Generation (RAG) techniques to provide accurate and contextually relevant responses, leveraging Moniepoint-specific knowledge.

## Features
- **Intelligent Query Resolution**: Uses RAG to retrieve and generate answers based on Moniepoint’s content.
- **Chat Interface**: A user-friendly interface powered by Streamlit for seamless interaction.
- **High-Performance Models**: Integrates with Together API for natural language understanding and generation.
- **Customizable Knowledge Base**: Automatically fetches relevant data using IlimiKudi.

## Technology Stack
- **AI Models**: Together API
- **Frameworks**:
  - txtai for embedding-based retrieval
  - LangChain for workflow orchestration
- **Frontend**: Streamlit for the chat interface
- **Backend**:
  - Python for core logic
  - RAG for combining retrieval with generative capabilities

## Installation
### Prerequisites
Ensure the following are installed on your system:
- Python 3.8 or higher
- Pip
- Virtualenv (recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/thelaycon/danjuma.git
   cd danjuma
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```
5. Open your browser and navigate to `http://localhost:8501` to start interacting with Danjuma.

## Configuration
### Knowledge Base
Danjuma utilizes embeddings stored in the `moniepoint_index` for efficient retrieval and response generation. No additional directories for blog posts or articles are required.

### Environment Variables
Set the following environment variable as required:
- `LLM_API_KEY`: Your API key for Together API

## Usage
- Open the Streamlit interface.
- Enter your query into the chatbox.
- Danjuma retrieves relevant information and generates a response.

## Acknowledgements
- Moniepoint MFB for their content and support
- txtai for embedding-based search
- LangChain for robust AI workflows
- Together API for high-performance LLMs
- IlimiKudi for dynamic data retrieval
