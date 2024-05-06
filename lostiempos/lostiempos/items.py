import scrapy


class NoticiaItem(scrapy.Item):
    pagina = scrapy.Field()
    url = scrapy.Field()
    fecha = scrapy.Field()
    titulo = scrapy.Field()
    cuerpo = scrapy.Field()
