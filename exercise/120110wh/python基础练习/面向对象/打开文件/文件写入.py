# 文件的读取
file_name = "hello\\logFile1.py"

# 使用open()打开文件时必须要指定打开文件所要作的操作（读、写、追加）
# 如果不指定操作类型，则默认是读取文件 而读取文件时是不能向文件中写入的
# r 表示只读
# w 表示是可写的，使用w来写入文件时，如果文件不存在，它会创建文件，如果存在则会截断文件
# 截断文件指删除原来文件中的所有内容
# a 表示追加内容
# + 为操作符增加功能
# r+
# w+
# a+
with open(file_name,"a",encoding="utf-8",) as file_obj:
    #write()来向文件中写入内容
    #如果操作的是一个文本文件的话，则write()需要传递一个字符串作为参数
    #该方法会可以分多次写入内容
    #写入成功后，该方法会返回写入的字符的个数
    file_obj.write("print('hello world!')\n")
