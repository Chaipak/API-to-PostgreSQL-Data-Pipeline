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

if __name__ == "__main__":
    from fetch_api import fetch_data  # Import fetch function

    raw_data = fetch_data()
    cleaned_data = clean_data(raw_data)

    print(cleaned_data[:3])  # Print first 3 cleaned records