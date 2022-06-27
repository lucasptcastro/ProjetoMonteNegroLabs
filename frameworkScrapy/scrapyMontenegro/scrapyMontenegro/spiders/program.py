import scrapy


class ProgramSpider(scrapy.Spider):
    name = 'program'
    start_urls = ['https://www.contabeis.com.br/conteudo/contabil/']

    def parse(self, response):
        for box in response.css('.editoria-contabil')[3:-1]:
            yield{
                'title': box.css('h2::text').get(),
                'category': box.css('strong::text').get(),
                'time': box.css(".timestamp::text").get(),
                'link': box.css('.compartilhamento::attr(href)').get()
            }

