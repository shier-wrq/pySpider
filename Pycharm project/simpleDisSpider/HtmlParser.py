#coding:utf-8
"""
HTML解析器
"""
import re
import urllib3
from bs4 import BeautifulSoup

class HtmlParser(object):

    def parser(self, page_url, html_cont):
        """
        用于解析网页内容，抽取URL和数据
        :param page_url:
        :param html_cont:
        :return:
        """
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        """
        抽取新URL集合
        :param page_url:
        :param soup:
        :return:
        """
        new_urls = set()
        #抽取符合要求的a标记
        links = soup.find_all("a", href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            #提取href属性
            new_url = link['href']
            #拼接成完整网址
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        """
        抽取有效数据
        :param page_url:
        :param soup:
        :return:
        """
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_='lemmaWgt-lemaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        data['summary'] = summary.get_text()

        return data
