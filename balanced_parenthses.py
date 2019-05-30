#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :19-5-17 下午9:38
# @Author  : liuyaanng
# @FileName: balanced_parenthses.py
# @Software: PyCharm Community Edition

from Self_data_struct_1 import *

def balanced_parenthese(data):
	stack = Stack(len(data))
	for i in data:
		if i == '(':
			stack.push(i)
		elif i == ')':
			if stack.is_empty():
				return False
			stack.pop()
	return stack.is_empty()

if __name__ == '__main__':
	data = '((()'
	p = balanced_parenthese(data)
	print(p)

