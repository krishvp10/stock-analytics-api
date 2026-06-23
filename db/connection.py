import os
import psycopg2 as pg

def get_connection():
    conn = pg.connect(
        dbname=os.getenv("DB_NAME", "stock"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "krish@psql"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432")
    )
    print("Connected to the database successfully")
    return conn