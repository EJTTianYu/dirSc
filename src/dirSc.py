#coding=utf-8

import os


file0=r'/Users/tianyu/iotdb-benchmark/src/main/java/cn/edu/tsinghua/iotdb/benchmark/db/opentsdb/OpenTSDB.java'

#读取文件的行数
def count_fileR(file):
    with open(file,'r',encoding='utf-8') as f:
        num=len(f.readlines());
    return num

print(count_fileR(file0))