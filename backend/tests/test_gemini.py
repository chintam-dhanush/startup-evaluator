from backend.services.llm.gemini_service import ask_gemini

response = ask_gemini("Say hello in one sentence.")

print(response)