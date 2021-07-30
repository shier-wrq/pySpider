#coding:utf-8
"""
控制调度器
"""
import atexit
import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import Process
from simpleDisSpider import URLManger
from simpleDisSpider import DataOutput

class StartControl(object):
    def start_Manager(self, url_q, result_q):
        """
        创建一个分布式管理器
        :param url_q:
        :param result_q:
        :return:
        """
        BaseManager.register('get_task_queue', callable = lambda:url_q)
        BaseManager.register('get_result_queue', callable = lambda: result_q)
        manager = BaseManager(address=('',8080), authkey='baike')
        return manager

    def url_manager_proc(self, url_q, conn_q, root_url):
        """
        URL管理进程将从conn_q队列获取到新的URL提交给URL管理器，经过去重后，去除URL
        放入url_queue队列中传递给爬虫节点
        :param url_q:
        :param conn_q:
        :param root_url:
        :return:
        """
        url_manager = URLManger()
        url_manager.add_new_url(root_url)
        while True:
            while(url_manager.has_new_url()):
                #从URL管理器获取新的URL
                new_url = url_manager.get_new_url()
                #将新的URL发给工作节点
                url_q.put(new_url)
                print('old_url=', url_manager.old_url_size())
                if(url_manager.old_url_size > 2000):
                    #通知爬行节点工作结束
                    url_q.put('end')
                    print('控制节点发起结束通知')
                    #关闭管理节点，同时存储set状态
                    url_manager.save_progress('new_urls.txt', url_manager.new_urls)
                    url_manager.save_progress('old_urls.txt', url_manager.old_urls)
                    return
            #将从resul_solve_proc获取到的URL添加到URL管理器
            try:
                if not  conn_q.empty():
                    urls = conn_q.get()
                    url_manager.add_new_urls(urls)
            except BaseException as e:
                time.sleep(0.1)#延时休息

    def result_solve_proc(self, result_q, conn_q, store_q):
        """
        数据提取进程从result_queue队列读取返回的数据，并将数据中的URL添加到conn_q
        队列交给URL管理进程，将数据中的文章标题和摘要添加到store_q队列交给数据存储进程
        :param result_q:
        :param conn_q:
        :param store_q:
        :return:
        """
        while(True):
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    if content['new_urls'] == 'end':
                        #结果分析进程接收通知然后结束
                        print('结果分析进程接收通知然后结束！')
                        store_q.put('end')
                        return
                    conn_q.put(content['news_urls'])#url为set类型
                    store_q.put(content['data'])#解析出来的数据为dict类型
                else:
                    time.sleep(0.1)#延时休息
            except BaseException as e:
                time.sleep(0.1)#延时休息

    def store_proc(self, store_q):
        output = DataOutput()
        while True:
            if not store_q.empty():
                data = store_q.get()
                if data == 'end':
                    print('存储进程接收通知然后结束')
                    output.output_end(output.filepath)
                    return
                output.store_data(data)
            else:
                time.sleep(0.1)
if __name__=='__main__':
    #初始化四个队列
    url_q = Queue()
    result_q = Queue()
    store_q = Queue()
    conn_q = Queue()
    #创建分布式管理器
    node = NodeManager()
    manager = node.start_Manger(url_q, result_q)
    #创建URL管理进程、数据提取进程、数据存储进程
    url_manager_proc = Process(target=node.url_manager_proc, args=(url_q, conn_q, 'http://baike.baidu.com/view/284853.htm',))
    result_solve_proc = Process(target=node.result_solve_proc, args=(result_q, conn_q, store_q,))
    store_proc = Process(target=node.store_proc, args=(store_q,))
    #启动3个进程和分布式管理器
    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()
    manager.get_server().serve_forever()

