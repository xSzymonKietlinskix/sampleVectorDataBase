import chromadb
from pprint import pprint
def chroma_sample(query,n_results=1):
    client = chromadb.Client()

    collection = client.create_collection('all-documents')

    collection.add(
        documents=[
            "Document about food",
            "Document about animals food",
            "Document about cats and dogs",
        ],
        metadatas=[{"topic": "food"}, {"topic": "animal"}, {"topic": "animal"}],
        ids=["doc1", "doc2", "doc3"],
    )

    results = collection.query(
        query_texts=[query],
        n_results=n_results,
    )

    pprint(results)
