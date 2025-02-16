def clean_data(data):
    """Process and clean the API data before inserting into the database"""
    cleaned_data = []
    
    for item in data:
        cleaned_data.append({
            "user_id": item.get("userId"),  # Convert key names if necessary
            "title": item.get("title").strip().capitalize(),
            "body": item.get("body").strip()
        })
    
    return cleaned_data