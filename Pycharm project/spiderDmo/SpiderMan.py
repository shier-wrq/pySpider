#coding utf-8
"""
爬虫调度器
"""
from spiderDmo.DataOutPut import DataOutPut
from spiderDmo.HtmlParser import HtmlParser
from spiderDmo.HtmlDownloader import HtmlDownloader
from spiderDmo.URLManager import UrlManager

class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutPut()

    def crawl(self, root_url):
        #添加入口URL
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print("已经抓取%s个链接"%self.manager.old_url_size())
            except Exception as e:
                print("crawl failed")
        self.output.output_html()

if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl("http://baike.baidu.com/view/284853.htm")
