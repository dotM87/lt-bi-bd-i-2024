import libsql_experimental as libsql
import os
from dotenv import load_dotenv
from .items import NoticiaItem

load_dotenv()

url = os.getenv("TURSO_DATABASE_URL")
auth_token = os.getenv("TURSO_AUTH_TOKEN")

class TursoPipeline:
    def open_spider(self, spider):
        self.conn = libsql.connect("lt-bi-bd", sync_url=url, auth_token=auth_token)
        self.conn.sync()
    
    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
            data = {
                'pagina': item['pagina'],
                'url': item['url'],
                'fecha': item['fecha'],
                'titulo': item['titulo'],
                'cuerpo': item['cuerpo']
            }
            query = "INSERT INTO noticias (pagina, url, fecha, titulo, cuerpo) VALUES (f'{data['pagina']}', f'{data['url']}', f'{data['fecha']}', f'{data['titulo']}', f'{data['cuerpo']}')"
            self.conn.execute(query)
            return item