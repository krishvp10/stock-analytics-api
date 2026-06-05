import psycopg2 as pg

def get_connection():
    conn =  pg.connect("dbname=stock user=postgres password=krish@psql port=5432")
    print("Connected to the database successfully")
    return conn
