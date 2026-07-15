import json
from rag.chroma_db import client

# Delete and recreate the collection to clear out old documents
try:
    client.delete_collection("government_schemes")
    print("Deleted old government_schemes collection.")
except Exception:
    print("Collection did not exist. Creating fresh...")

collection = client.get_or_create_collection(
    name="government_schemes"
)

with open(
    "data/government_schemes.json",
    "r",
    encoding="utf-8"
) as f:
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