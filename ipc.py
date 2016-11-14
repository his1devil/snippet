#! /usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing

"""
生产者消费者模式
生产者将项目放入队列，等待处理
消费者设置为deamon，always运行
"""
def consumer(input_q):
    while True:
        item = input_q.get() # 返回项目
        print item
        # 信号通知完成
        input_q.task_done()

def producer(sequence, output_q):
    for item in sequence:
        # 将项目放入队列
        output_q.put(item)


if __name__ == '__main__':
    """
    创建一个可连接的共享进程队列，就像一个Queue对象，但队列允许项目的消费者通知生产者
    项目已经被成功处理，通知进程是使用共享的信号和条件变量来实现
    """
    q = multiprocessing.JoinableQueue()
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.daemon = True
    cons_p.start()

    sequence = [1, 2, 3, 4]
    producer(sequence, q)

    q.join() # 等待所有项目被处理
