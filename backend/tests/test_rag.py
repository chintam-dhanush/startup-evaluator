from rag.retrieve import retrieve_schemes

query = """
AI startup for farmers to detect crop diseases using computer vision
"""

results = retrieve_schemes(query)

import json
try:
    print(json.dumps(results, indent=2))
except UnicodeEncodeError:
    print(json.dumps(results, indent=2).encode('ascii', errors='replace').decode('ascii'))