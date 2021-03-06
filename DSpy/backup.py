# Spider to scrape quotes.toscrape.com

import scrapy
from ..items import DspyItem

class QuoteScapper(scrapy.Spider):

	name = "quotes"
	start_urls = ['http://quotes.toscrape.com/']

	def parse(self,response):

		items = DspyItem()

		all_div_quotes = response.css("div.quote")
		for quote in all_div_quotes:
			title = quote.css("span.text::text").extract()
			author = quote.css(".author::text").extract()
			tag = quote.css(".tag::text").extract()

			items['title'] = title
			items['author'] = author
			items['tag'] = tag

			yield items

		next_page = response.css("li.next a::attr(href)") 
		# for pagination if pages present as integers, take a class variable as page number, add it to the base url after making it as a string
		if next_page is not None:
			yield response.follow(next_page, callback = self.parse)