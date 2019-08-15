# 包 （package）
# 包也是一个模块
# 当我们模块中代码过多时，或者一个模块需要被分解为多个模块时，这是就需要使用到包
# 普通的模块就是一个py文件，而包时一个文件夹
#   包中必须要有一个__init__.py这个文件

from hello import a , b

print(a.c)
print(b.d)

# __pycache__是模块的缓存文件
# py代码在执行前，需要被解析器先转换为机器码，然后再执行
#  所以我们再使用模块（包）时，也需要将模块的代码先转换成机器码然后再交由计算机执行
#  而为了提高程序运行的性能，python会在编译过一次以后，将代码保存到一个缓存文件中
#  这样再下次加载这个模块（包）时，就可以不再重新编译而是直接加载缓存中编译好的代码即可
