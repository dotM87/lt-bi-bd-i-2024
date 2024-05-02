import scrapy

class ResultadosSpider(scrapy.Spider):
    name = 'resultados'
    start_urls = ['https://www.lostiempos.com/hemeroteca?contenido=&sort_by=field_noticia_fecha&page=0']
    
    def parse(self, response):
        # Obtener los elementos <a> con las URL de los resultados
        for resultado in response.css('.view-content .views-row .views-field-title a'):
            url = resultado.attrib['href']
            yield {
                'url': url,
            }
            print(url)

        # Obtener la URL de la siguiente página de resultados
        next_page = response.css('.pager-next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

