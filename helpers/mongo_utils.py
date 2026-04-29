def format_one_with_password(doc: dict | None) -> dict | None:
    """Safely converts a single MongoDB document's _id to a string."""
    if not doc:
        return None
    formatted_doc = {**doc, "_id": str(doc["_id"])}
    
    # # Optional: Automatically hide passwords when fetching data!
    # formatted_doc.pop("password", None) 
    
    return formatted_doc

def format_one(doc: dict | None) -> dict | None:
    if not doc:
        return None
    formatted_doc = {**doc, "_id": str(doc["_id"])}
    formatted_doc.pop("password", None)  
    return formatted_doc

def format_list(docs: list[dict]) -> list[dict]:
    return [format_one(doc) for doc in docs]