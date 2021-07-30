#coding:utf-8
"""
数据存储器
"""
import codecs
import time
class DataOutPut(object):

    def __init__(self):
        self.filepath = 'baike_%s.html'%(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
        self.output_head(self.filepath)
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) > 10:
            self.output_html(self.filepath)

    def output_head(self, path):
        """
        HTML开始
        :param path:
        :return:
        """
        fout = codecs.open(path, 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        fout.close()

    def output_html(self, path):
        """
        将数据写入HTML文件
        :param path:
        :return:
        """
        fout = codecs.open(path, 'a', encoding='utf-8')#a：附加写方式打开，不可读；a+: 附加读写方式打开
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
            self.datas.remove(data)
        fout.close()

    def output_end(self, path):
        """
        HTML结束
        :param path:
        :return:
        """
        fout = codecs.open(path, 'a', encoding='utf-8')
        fout.write("</html>")
        fout.write("</body>")
        fout.write("</table>")
        fout.close()

