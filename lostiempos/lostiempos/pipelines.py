import pandas as pd
from .items import NoticiaItem

class ParquetPipeline:
    def open_spider(self, spider):
        self.items = []
    
    def close_spider(self, spider):
        df = pd.DataFrame(self.items)
        df.to_parquet('noticias.parquet', engine='pyarrow')

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item

