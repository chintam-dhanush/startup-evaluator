from pathlib import Path
import chromadb

# backend/
BASE_DIR = Path(__file__).resolve().parent.parent

# backend/chroma_db/
DB_PATH = BASE_DIR / "chroma_db"

client = chromadb.PersistentClient(path=str(DB_PATH))

collection = client.get_or_create_collection(
    name="government_schemes"
)