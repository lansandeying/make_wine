#coding=utf-8
from multiprocessing import Process
import os

def num():
    try:
        1>0
    except Exception as e:
        pass
    raise Exception("主动异常")
    return print("A")

try:
    num()
    print("houmian")
except Exception as e:
    print(e)

