# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# scrapped data -> Item container -> json/csv/xml
# scaped data -> Item container -> Pipeline -> SQL/MONGO DB database



class DspyPipeline:
    def process_item(self, item, spider):

    	print("Pipeline ", item['title'])