import os
import libsql_experimental as libsql
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("TURSO_DATABASE_URL")
auth_token = os.getenv("TURSO_AUTH_TOKEN")

conn = libsql.connect("lt-bi-bd", sync_url=url, auth_token=auth_token)
conn.execute("CREATE TABLE IF NOT EXISTS noticias (id SERIAL PRIMARY KEY, pagina TEXT, url TEXT, fecha TEXT, titulo TEXT, cuerpo TEXT)")
conn.commit()
print(conn.execute("SELECT * FROM noticias").fetchall())