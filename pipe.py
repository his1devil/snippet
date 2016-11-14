#! /usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing


def consumer(pipe):
    output_p, input_p = pipe
    input_p.close() # 关闭管道输入流
    while True:
        try:
            item = output_p.recv()
        except EOFError:
            break
        print item
    print "Consumer done"

def producer(sequence, input_p):
    for item in sequence:
        input_p.send(item)


if __name__ == '__main__':
    (output_p, input_p) = multiprocessing.Pipe() # 返回的元组表示管道两端的连接对象, 默认双向
    # 启动消费者进程
    cons_p = multiprocessing.Process(target=consumer, args=((output_p, input_p)))
    cons_p.start()

    # 关闭生产者中的输出管道
    output_p.close()

    # 生产项目
    sequence = [1, 2, 3, 4]
    producer(sequence, input_p)

    # 关闭输入管道，表示完成
    input_p.close()

    # 等待消费者进程关闭
    cons_p.join()
