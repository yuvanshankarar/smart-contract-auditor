import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="smart_contract_docs"
)

print("ChromaDB Connected")
print("Collection:", collection.name)