##RAG System with Local Qdrant and Mistral 7B

This repository contains a script for a Retrieval-Augmented Generation (RAG) system, leveraging a local Qdrant vector database and a Mistral 7B language model. This setup is designed for efficient passage retrieval and natural language response generation.

Prerequisites

Python 3.8+

Docker (for running the Qdrant server)

Qdrant Client and Requests Python packages

A local LLM server with Mistral 7B and mxbai-embed-large models.

Install Required Packages

Run the following command to install the required dependencies using the UV package manager:

uv install qdrant-client requests

Setting Up the Qdrant Vector Database

You need to start a Qdrant server for this project. If you don't have it installed, you can use Docker:

docker run -p 6333:6333 -v qdrant_storage:/qdrant/storage qdrant/qdrant

For more detailed installation and configuration, refer to the Qdrant documentation.

Once the Qdrant server is running, the script will create a collection named "demo" if it does not already exist.

Adding Dummy Data to Qdrant

Before running the main script, you should create and store your own dummy data. Uncomment the relevant section in the script to populate the Qdrant collection with sample passages. For example:

dummy_data=[
    "My name is Erick",
    "I like watching football",
    "I like learning new stuff",
    "I like cats",
    "I like dogs"
]

Make sure to replace this with your own representative data and then comment out the other codeblocks until data is saved to qdrant.

Local LLM Setup

Ensure you have the following models available on your local LLM server:

Mistral 7B for response generation

mxbai-embed-large for text embeddings

Your local server should expose endpoints as shown in the script (e.g., http://localhost:11434/api/generate for text generation and http://localhost:11434/api/embed for embeddings).

Running the Script

Start your Qdrant Docker container and local LLM server, then run:

uv run main.py

How It Works

The script accepts a prompt from the user.

It adjusts the prompt for optimal passage retrieval.

The adjusted prompt is converted to a vector using the mxbai-embed-large model.

Relevant passages are retrieved from the Qdrant database.

The retrieved passages are used to generate a context-aware response via the Mistral 7B model.

The response is printed to the console.

Contributing

Feel free to fork this repository and contribute to improve this RAG setup. Pull requests are welcome.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Support

For support, open an issue or reach out directly.