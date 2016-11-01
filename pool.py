#! /usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Pool
import contextlib
from time import sleep

def start_function_for_processes(n):
    sleep(.5)
    result_sent_back_to_parent = n * n
    return result_sent_back_to_parent

if __name__ == '__main__':
    with contextlib.closing(Pool(processes=5)) as p:
        results = p.map(start_function_for_processes, range(200), chunksize=10)
    print results
