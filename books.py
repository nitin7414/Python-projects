import scrapy 

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]    #get the file using scrapy built-in function

    def parse(self, response):
        for book in response.css('article.product_pod'):     #iterate through each element with the same tag and extaract the text of it
            yield {
                'title':book.css('h3 a::text').get(),
                'price':book.css('p.price_color::text').get()
            }
        next_page = response.css('li.next a::attr(href)').get()       #Check for next page as well, and if there exists, then use the smae funtion as above to extract data/
        if next_page:
            yield response.follow(next_page, callback = self.parse)

