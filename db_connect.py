import psycopg2
from db_hide import database_name, database_host, database_port, database_password, database_username

DB_NAME = database_name
DB_USER = database_username
DB_PASS = database_password
DB_HOST = database_host
DB_PORT = database_port

conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST, port=DB_PORT)

cur = conn.cursor()

print('Database successful connection!')