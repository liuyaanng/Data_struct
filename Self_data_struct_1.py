#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :19-5-17 下午9:15
# @Author  : liuyaanng
# @FileName: Self_data_struct_1.py
# @Software: PyCharm Community Edition


# 栈
class Stack(object):
	def __init__(self, limit = 10):
		self.stack = []
		self.limit = limit
	# 	limit为栈的上限
	def __str__(self):
		printed = '<' + str(self.stack)[1:-1] + '>'
		return printed
	def push(self, data):
		if len(self.stack) >= self.limit:
			print('StackOverflowError')
			pass
		self.stack.append(data)

	def pop(self):
		if self.stack:
			return self.stack.pop()
		else:
			raise IndexError('pop from an empty stack')
	# 	空栈不能弹出数据

	#   弹出栈顶元素
	def peek(self):
		if self.stack:
			return self.stack[-1]
		else:
			raise IndexError('stack is empty')
	# 	判空
	def is_empty(self):
		return not bool(self.stack)
	#   栈大小
	def size(self):
		return len(self.stack)




# 链表(单链表)
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None #表示下一个链接的链点

class Linked_List(object):
	def __init__(self):
		self.head = None #链表的头部元素
	def initlist(self, data_list):
		self.head = Node(data_list[0])
		temp = self.head
		for i in data_list[1:]:
			node = Node(i)
			temp.next = node
			temp = temp.next

	def is_empty(self):
		return self.head is None

	def insert(self, key, value):
		if key < 0 or key > self.get_length() - 1:
			print('insert error')
		temp = self.head
		i = 0
		while i < key:
			pre = temp
			temp = temp.next
			i += 1
		node = Node(value)
		pre.next = node
		node.next = temp

	def remove(self, key):
		if key < 0 or key > self.get_length() - 1:
			print('remove error')
		i = 0
		temp = self.head
		while temp != None:
			pre = temp
			temp = temp.next
			i += 1
			if i == key:
				pre.next = temp.next
				temp = None
				return True
		pre.next = None


	def get_length(self):
		temp = self.head
		length = 0
		while temp != None:
			length += 1
			temp = temp.next
		return length


	def print_list(self):
		print('Linked_list:')
		temp = self.head
		while temp is not None:
			print(temp.data)
			temp = temp.next

	def reverse(self):
		prev = None
		current = self.head
		while current:
			next_node = current.next
			current.next = prev
			prev = current
			current = next_node
		self.head = prev












































