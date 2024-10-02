import scrapy

class ProductosSpider(scrapy.Spider):
    name = 'textos'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

   
    def parse(self, response):
        # Extrae todas las citas de la página
        for quote in response.css('div.quote'):
            # Extraer el texto de la cita
            text = quote.css('span.text::text').get()
            # Extraer el autor (si es necesario)
            author = quote.css('span small.author::text').get()
            # Extraer las etiquetas (si es necesario)
            tags = quote.css('div.tags a.tag::text').getall()

            yield {
                'text': text,   
                'author': author,
                'tags': tags,
            }