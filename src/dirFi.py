#coding=utf-8

import os

file0=r'/Users/tianyu/iotdb-benchmark'
fileOut=r'/Users/tianyu/ioTDB_benchmark.txt'
#读取文件的行数
def count_fileR(file):
    with open(file,'r',encoding='utf-8') as f:
        num=len(f.readlines());
    return num
# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s%s' % (filepath,'/',allDir))

        try:
            with open(fileOut,'a',encoding='utf-8') as fout:
                if('.java' in child ) and('test' in child):
                    print(child[14:],count_fileR(child))

                    fout.write('|'+child[14:]+'|'+str(count_fileR(child))+'|'+'|'+'|'+'|'+'\n')
        except:
            pass
        try:
            eachFile(filepath+'/'+allDir)
        except:
            pass

eachFile(file0)
