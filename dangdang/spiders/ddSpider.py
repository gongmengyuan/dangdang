import scrapy
from bs4 import BeautifulSoup

from dangdang.items import DangdangItem


class DdspiderSpider(scrapy.Spider):
    name = 'ddSpider'
    allowed_domains = ['bang.dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-' + str(i) for i in range(1,11)]
    # scrapy crawl ddSpider -o dangdang.csv

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html, features="lxml")
        lis = soup.select(".bang_list_mode>li")
        # lis = response.css(".bang_list_mode>li")
        for li in lis:
            # 获取书名
            title = li.select(".name>a")[0].get("title")
            # 获取评论数
            ping_lun = li.select_one(".star>a").string
            # 获取作者
            publisher_info1 = li.select(".publisher_info")[0]
            author = publisher_info1.select("a")[0].string
            # 获取出版社
            publisher_info2 = li.select(".publisher_info")[1]
            publisher = publisher_info2.select("a")[0].string
            item = DangdangItem()
            item["title"] = title
            item["ping_lun"] = ping_lun
            item["author"] = author
            item["publisher"] = publisher
            # 获取书的详情页的链接地址
            href = li.select(".name>a")[0].get("href")
            yield scrapy.Request(url=href,
                                 callback=self.parse_detial,
                                 meta={"item": item},
                                 dont_filter=True,
                                 )


    def parse_detial(self, response):
        html = response.text
        soup = BeautifulSoup(html, features="lxml")
        tui_jian = soup.select(".name_info>h2>span")[0].string
        item = response.meta["item"]
        item["tui_jian"] = tui_jian
        yield item


