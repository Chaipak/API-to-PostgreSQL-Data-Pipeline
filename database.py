import psycopg2
from config import DB_CONFIG

def connect_db():
    """Establish a connection to PostgreSQL"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✅ Connected to PostgreSQL successfully!")
        return conn
    except Exception as e:
        print(f"❌ Database connection error: {e}")
        return None

def create_table():
    """Create the posts table if it does not exist"""
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
            print("📌 Creating table 'posts'...")
            cur.execute("""
                CREATE TABLE IF NOT EXISTS posts (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER,
                    title TEXT,
                    body TEXT
                )
            """)
            conn.commit()
            cur.close()
            conn.close()
            print("✅ Table 'posts' created successfully!")
        except Exception as e:
            print(f"❌ Error creating table: {e}")
            conn.close()
            
def insert_data(data):
    """Insert cleaned API data into the PostgreSQL database"""
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
            print("📌 Inserting data into 'posts' table...")

            for item in data:
                cur.execute("""
                    INSERT INTO posts (user_id, title, body) VALUES (%s, %s, %s)
                """, (item["user_id"], item["title"], item["body"]))
            
            conn.commit()
            cur.close()
            conn.close()
            print(f"✅ Inserted {len(data)} records into the database.")
        except Exception as e:
            print(f"❌ Error inserting data: {e}")
            conn.close()