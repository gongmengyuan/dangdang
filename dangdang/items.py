# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    # 评论
    ping_lun = scrapy.Field()
    author = scrapy.Field()
    publisher = scrapy.Field()
    # 推荐理由
    tui_jian = scrapy.Field()

    pass
