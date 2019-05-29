#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :19-5-24 下午5:56
# @Author  : liuyaanng
# @FileName: Self_data_struct_3.py
# @Software: PyCharm Community Edition


# binary_tree

class Node(object):
	def __init__(self,item):
		self.item = item
		self.left = None
		self.right = None
	def __str__(self):
		return str(self.item)

class Tree(object):
	def __init__(self):
		self.root = Node('root')  #根节点定义为root永不删除，作为哨兵

	def add(self, item):
		node = Node(item)
		if self.root is None:
			self.root = node
		else:
			q = [self.root]
			while True:
				pop_node = q.pop(0)
				if pop_node.left is None:
					pop_node.left = node
					return
				elif pop_node.right is None:
					pop_node.right = node
					return
				else:
					q.append(pop_node.left)
					q.append(pop_node.right)




