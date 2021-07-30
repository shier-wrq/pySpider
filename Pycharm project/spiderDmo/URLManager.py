#coding:utf-8
"""
URL管理器
"""
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()#未爬取的URL集合
        self.old_urls = set()#已爬取的URL集合

    def new_url_size(self):
        return len(self.new_urls)

    def old_url_size(self):
        return len(self.old_urls)

    def has_new_url(self):
        '''
        判断是否有未爬取的URL
        :return:
        '''
        return self.new_url_size() != 0;

    def get_new_url(self):
        """
        获取一个未爬取的URL
        :return:
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        """
        将新的URL添加到未爬取的URL集合中
        :param url:
        :return:
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        同上 不过是集合
        :param urls:
        :return:
        """
        if urls is None and len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
