#coding:utf-8
"""
URL管理器
"""
import pickle
import hashlib
class UrlManager(object):
    def __init__(self):
        self.new_urls = self.load_progress('new_urls.txt')#未爬取的URL集合
        self.old_urls = self.load_progress('old_urls.txt')#已爬取的URL集合

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
        m = hashlib.md5();#获取一个md5加密算法对象
        m.update(new_url)
        self.old_urls.add(m.hexdigest()[8:-8])#获取加密后的16进制字符串
        return new_url

    def add_new_url(self, url):
        """
        将新的URL添加到未爬取的URL集合中
        :param url:
        :return:
        """
        if url is None:
            return
        m = hashlib.md5()
        m.update(url)
        url_md5 = m.hexdigest()[8:-8]
        if url not in self.new_urls and url_md5 not in self.old_urls:
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
    """
    save_progress()和load_progress()是为了进行序列化操作
    将未爬取的URL集合和已经爬取的URL集合序列化到本地，保存当前的进度，以便下次恢复状态
    """

    def save_progress(self, path, data):
        """
        保存进度
        :param path:
        :param data:
        :return:
        """
        with open(path, 'wb') as f:
            """
            dumps()：将 Python 中的对象序列化成二进制对象，并返回;
            dump()：将 Python 中的对象序列化成二进制对象，并写入文件;
            """
            pickle.dump(data, f)

    def load_progress(self, path):
        """
        从本地文件加载进度
        :param path:
        :return:
        """
        print('[+]从文件加载进度: %s'%path)
        try:
            with open(path, 'rb') as f:
                """
                loads()：读取给定的二进制对象数据，并将其转换为 Python 对象;
                load()：读取指定的序列化数据文件，并返回对象;
                """
                tmp = pickle.load(f)
                return tmp
        except:
            print('[!]无进度文件，创建: %s' % path)
        return set()

