# Spider to scrape quotes.toscrape.com

import scrapy
from ..items import DspyItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class QuoteScapper(scrapy.Spider):

	name = "quotes"
	start_urls = ['http://quotes.toscrape.com/login']

	def start_scrapy(self,response):
		open_in_browser(response)

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

	def parse(self,response):
		token = response.css("form input::attr(value)").extract_first()
		return FormRequest.from_response(response, formdata={
			'csrf_token':token,
			'username': 'iamuser',
			'password':'I wont tell you'
			}, callback=self.start_scrapy)
