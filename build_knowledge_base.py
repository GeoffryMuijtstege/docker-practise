import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("docs")

with open("profile.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["geoffry"])

print("Embedding stored in Chroma")