from rag.chroma_db import collection
from rag.ingest import ingest_database

def ensure_database():
    if collection.count() == 0:
        print("📦 Building vector database...")
        ingest_database()
        print("✅ Done.")
    else:
        print(f"✅ ChromaDB ready ({collection.count()} documents)")