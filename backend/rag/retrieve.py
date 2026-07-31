from sentence_transformers import SentenceTransformer
from rag.chroma_db import collection

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_schemes(query, top_k=3):

    embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    if (
    not results.get("documents")
    or not results["documents"]
    or not results["documents"][0]
    ):
        return []

    schemes = []

    documents = results["documents"][0]
    metadata = results["metadatas"][0]

    for doc, meta in zip(documents, metadata):

        schemes.append({
            "scheme_name": meta.get("scheme_name", ""),
            "ministry": meta.get("ministry", ""),
            "state": meta.get("state", ""),
            "description": meta.get("description", ""),
            "benefits": meta.get("benefits", ""),
            "eligibility": meta.get("eligibility", ""),
            "application_link": meta.get("application_link", ""),
            "sector": meta.get("sector", "").split(",") if meta.get("sector") else [],
            "stage": meta.get("stage", "").split(",") if meta.get("stage") else []
        })

    print(f"Retrieved {len(schemes)} government schemes.")

    return schemes