from fetch_api import fetch_data
from process_data import clean_data
from database import create_table, insert_data

def main():
    """Run the full API-to-PostgreSQL pipeline."""
    print("🚀 Starting data pipeline...")

    # Step 1: Fetch data from the API
    raw_data = fetch_data()
    if not raw_data:
        print("❌ No data fetched. Exiting.")
        return

    # Step 2: Process and clean the data
    cleaned_data = clean_data(raw_data)

    # Step 3: Ensure the database table exists
    create_table()

    # Step 4: Insert processed data into the database
    insert_data(cleaned_data)

    print("✅ Data pipeline completed successfully!")

if __name__ == "__main__":
    main()