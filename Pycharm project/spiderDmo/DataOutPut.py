#coding:utf-8
"""
数据存储器
"""
import codecs
class DataOutPut(object):

    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        """
        将数据写入HTML文件
        :return:
        """
        fout = codecs.open('baike.html', 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
            self.datas.remove(data)
        fout.write("</html>")
        fout.write("</body>")
        fout.write("</table>")
        fout.close()