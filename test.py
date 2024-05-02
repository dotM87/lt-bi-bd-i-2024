import libsql_experimental as libsql
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("TURSO_DATABASE_URL")
auth_token = os.getenv("TURSO_AUTH_TOKEN")

conn = libsql.connect("lt-bi-bd", sync_url=url, auth_token=auth_token)
conn.sync()
