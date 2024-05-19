import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from .items import NoticiaItem

class ParquetPipeline:
    def open_spider(self, spider):
        self.schema = pa.schema([
            ('pagina', pa.string()),
            ('url', pa.string()),
            ('fecha', pa.date64()),
            ('titulo', pa.string()),
            ('cuerpo', pa.string())
        ])
        self.items = []

    def close_spider(self, spider):
        table = pa.Table.from_pandas(pd.DataFrame(self.items), schema=self.schema)
        pq.write_table(table, 'noticias.parquet')

    def process_item(self, item, spider):
        self.items.append({
            'pagina': item['pagina'],
            'url': item['url'],
            'fecha': item['fecha'],
            'titulo': item['titulo'],
            'cuerpo': item['cuerpo']
        })
        return item
