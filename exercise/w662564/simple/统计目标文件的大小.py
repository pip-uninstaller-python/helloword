#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 13:28
# @Author  : 錵滊嫣缘
# @File    : 统计目标文件的大小.py
# @Software: PyCharm

# 导入os模块
import  os
sum = 0#
# 定义一个全局变量存储计算之后的值
def file_statistics(file):
    '''
    定义一个函数计算文件夹的大小
    :param file: 文件夹的路径，不能是中文字符的文件夹名
    :return:返回文件的大小字节数
    '''
    global sum
    ls =os.listdir(file) #目录下的所有文件和目录名传转成列表形式赋值给ls。
    # 遍历整个文件夹
    for i in ls:
        # 如果是文件的情况下用函数getsize 求出文件的大小复制给sum
        if os.path.isfile(os.path.join(file, i)):

            sum +=os.path.getsize(os.path.join(file,i))
        # 反之如果是文件夹则进行递归操作直到找到文件为止
        else:
             file_statistics(os.path.join(file,i))
    # 返回文件的大小值
    return sum

if __name__ == '__main__':#这句话其实我也知道干嘛的就知道这么用😁

    print(file_statistics(input('输入要测试的文件夹(不可用中文的文件名):')),'字节')
    # 如文件夹C:\Program Files (x86)  都可以测试

