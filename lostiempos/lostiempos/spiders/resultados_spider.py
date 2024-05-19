import scrapy
from lostiempos.items import NoticiaItem

class NoticiasSpider(scrapy.Spider):
    name = 'noticias'
    allowed_domains = ['lostiempos.com']
    start_urls = ['https://www.lostiempos.com/hemeroteca?contenido=&sort_by=field_noticia_fecha&page=0']
    
    def parse(self, response):
        # Obtener los elementos <a> con las URL de los resultados
        for resultado in response.css('.view-content .views-row'):
            item = NoticiaItem()
            item['pagina'] = 'Los Tiempos'
            item['url'] = "https://www.lostiempos.com" + resultado.css('.views-field-title a::attr(href)').get()
            item['fecha'] = resultado.css('.date-display-single::text').get()
            item['titulo'] = resultado.css('.views-field-title a::text').get()
            yield response.follow(item['url'], self.parse_noticia, meta={'item': item})
            
        # Obtener la URL de la siguiente página de resultados
        next_page = response.css('.pager-next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_noticia(self, response):
        item = response.meta['item']
        item['cuerpo'] = ' '.join(response.css('.field-name-body .field-item p::text').extract())
        print(item)
        yield item

