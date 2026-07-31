import json
from rag.chroma_db import client
from pathlib import Path

def ingest_database():
    
    # Delete and recreate the collection to clear out old documents
    try:
        client.delete_collection("government_schemes")
        print("Deleted old government_schemes collection.")
    except Exception:
        print("Collection did not exist. Creating fresh...")

    collection = client.get_or_create_collection(
        name="government_schemes"
    )


    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_FILE = BASE_DIR / "data" / "government_schemes.json"

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        schemes = json.load(f)

    for scheme in schemes:
        document = f"""
    Scheme Name:
    {scheme["scheme_name"]}

    Description:
    {scheme["description"]}

    Benefits:
    {scheme["benefits"]}

    Eligibility:
    {scheme["eligibility"]}

    Sector:
    {", ".join(scheme["sector"])}

    Stage:
    {", ".join(scheme["stage"])}
    """

        collection.add(
            ids=[scheme["id"]],
            documents=[document],
            metadatas=[
                {
                    "scheme_name": scheme["scheme_name"],
                    "state": scheme["state"],
                    "ministry": scheme["ministry"],
                    "description": scheme["description"],
                    "benefits": scheme["benefits"],
                    "eligibility": scheme["eligibility"],
                    "application_link": scheme["application_link"],
                    "sector": ",".join(scheme["sector"]),
                    "stage": ",".join(scheme["stage"])
                }
            ]
        )

    print(f"Success: {len(schemes)} Government schemes added successfully!")



if __name__ == "__main__":
    ingest_database()