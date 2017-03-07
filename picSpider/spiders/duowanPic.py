# -*- coding: utf-8 -*-
import scrapy
from picSpider.items import PicspiderItem

class DuowanpicSpider(scrapy.Spider):
    name = "duowanPic"
    allowed_domains = ["duowan.com"]
    # 定义开始爬取的页面A
    start_urls = ["http://tu.duowan.com/scroll/132572.html"]
    def parse(self, response):
        # 定义获取数据的结构
        item = PicspiderItem()
        item['pic_url'] = response.selector.xpath(
            '//*[@id="picture-pageshow"]/div[1]/div[@class="pic-box"]/a/img/@src').extract()
        yield item