# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FizzyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Transaction(scrapy.Item):
    txHash = scrapy.Field()
    txReceiptStatus = scrapy.Field()
    blockHeight = scrapy.Field()
    timeStamp = scrapy.Field()
    fromAddress = scrapy.Field()
    toAddress = scrapy.Field()
    value = scrapy.Field()
    gasLimit = scrapy.Field()
    gasUsed = scrapy.Field()
    gasPrice = scrapy.Field()
    actualCost = scrapy.Field()
    nonce = scrapy.Field()
    inputData = scrapy.Field()