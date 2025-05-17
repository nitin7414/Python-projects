import scrapy 

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        for book in response.css('article.product_pod'):
            yield {
                'title':book.css('h3 a::text').get(),
                'price':book.css('p.price_color::text').get()
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback = self.parse)

