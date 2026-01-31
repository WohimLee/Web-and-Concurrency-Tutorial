
_llm_client = None

def get_llm_client():
    global _llm_client
    if _llm_client is None:
        _llm_client = ""
    return _llm_client
