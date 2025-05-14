import requests
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

client=QdrantClient(url="http://localhost:6333")
if not client.collection_exists(collection_name="demo"):
    client.create_collection(
        collection_name="demo",
        vectors_config=VectorParams(size=1024, distance=Distance.DOT),
    )

""" dummy_data=[
    "My name is Erick",
    "I Like Watching Football",
    "I like Learning new stuff",
    "I like Cats",
    "I like Dogs"
] """

def generate_response(prompt:str):
    response=requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral:7b",
            "prompt":prompt,
            "stream": False
        }
    )
    return response.json()["response"]


def main():
    # for i, text in enumerate(dummy_data):
    #     response=requests.post(
    #         "http://localhost:11434/api/embed",
    #         json={"model": "mxbai-embed-large", "input": text},
    #     )
    #     data=response.json()
    #     embeddings=data["embeddings"][0]
    #     client.upsert(
    #         collection_name="demo",
    #         wait=True,
    #         points=[PointStruct(id=i,vector=embeddings,payload={"text": text})]
    #     )
    prompt=input("Enter a Prompt: ")
    adjusted_prompt=f"Represent this sentence for searching relevant passages: {prompt}"
 

    # prompt=input("Enter a Prompt: ")
    # adjusted_prompt=f"Represent this sentence for searching relevant passages: {prompt}"

    response=requests.post(
        "http://localhost:11434/api/embed",
        json={"model": "mxbai-embed-large", "input": adjusted_prompt},
    )
    data=response.json()
    embeddings=data["embeddings"][0]

    results=client.query_points(
        collection_name="demo",
            query=embeddings,
            with_payload=True,
            limit=2
    )

    # for point in results.points:
    #     print(point.payload["text"])
    relevant_passages="\n".join([f"={point.payload['text']}" for point in results.points])
    augmented_prompt=f"""
    The Following are relevant passages:{relevant_passages},
    Answer the following question with the help of retrieved passages: {prompt}
    """
    
    response=generate_response(augmented_prompt)
    print(response)





if __name__=="__main__":
    main()
