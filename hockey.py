import scrapy

class HockeySpider(scrapy.Spider):     #This will use the funciton of scrapy library
    name = 'hockey'
    allowed_domains =['scrapethissite.com']
    start_urls = ["https://www.scrapethissite.com/pages/forms/"]    #placing the url here is must of the site

    def parse(self, response):
        for hock in response.css('tr.team'):         #The for loop will iterate through each loop and extract the data from the tag
            yield {
                'name':hock.css('td.name::text').get().strip(),
                'Debut-year': hock.css('td.year::text').get().strip(),
                'wins':hock.css('td.wins::text').get().strip()
            }

        next_page = response.css('ul.pagination li a::attr(href)').get()  # will check for the next page of site
        next_page_url = 'https://www.scrapethissite.com'+ next_page        # if next page is available then get the link
        if next_page:
            yield response.follow(next_page_url, callback = self.parse)     #follow the same functionality as above for each element with the tag in another page also