# first_script.py —— 你的第一个 Python 脚本
# 运行方式:在该文件所在文件夹打开终端,执行: python first_script.py

import sys
sys.stdout.reconfigure(encoding="utf-8")   # Windows 控制台默认 GBK,打印 emoji/特殊字符会报错,统一改用 UTF-8

print("你好,世界! 🌱")

import numpy as np

# 脚本和 notebook 一样能用的库
a = np.array([[1, 2, 3],
              [4, 5, 6]])
print("矩阵形状:", a.shape)
print("矩阵乘 2:\n", a * 2)

# 试试改上面的数字,再运行一次,看输出变化