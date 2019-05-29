#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :19-5-24 上午11:45
# @Author  : liuyaanng
# @FileName: Self_data_struct_2.py
# @Software: PyCharm Community Edition


# 链表(双向链表)

class Node(object):
	def __init__(self, item):
		self.item = item
		self.next = None
		self.prev = None


class DLinkList(object):
	# 双向链表
	def __init__(self):
		self.head = None

	def is_empty(self):
		# 判断链表是否为空
		return self.head == None

	def get_length(self):
		# 返回链表的长度
		cur = self.head
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		# 遍历链表
		cur = self.head
		while cur != None:
			print(cur.item, end=' <---> ')
			cur = cur.next
		print("")

	def add(self, item):
		# 头部插入元素
		node = Node(item)
		if self.is_empty():
			# 如果是空链表，将head指向node
			self.head = node
		else:
			node.next = self.head
			self.head.prev = node
			self.head = node

	def append(self, item):
		# 尾部插入元素
		node = Node(item)
		if self.is_empty():
			self.head = node
		else:
			cur = self.head
			while cur.next != None:
				cur = cur.next
			cur.next = node
			node.prev = cur

	def search(self, item):
		# 查找元素是否存在
		cur = self.head
		while cur != None:
			if cur.item == item:
				return True
			cur = cur.next
		return False

	def insert(self, pos, item):
		# 在指定位置添加节点

		if self.is_empty() or pos <= 0:
			self.add(item)
		elif pos > self.get_length()-1:
			print("表长度不足，已插到末尾")
			self.append(item)
		else:
			node = Node(item)
			cur = self.head
			count = 0
			while count < pos-1:
				count += 1
				cur = cur.next
			cur.next.prev = node
			node.next = cur.next
			cur.next = node
			node.prev = cur
	def remove(self, item):
		# 删除一个节点
		if self.is_empty():
			print("链表为空,无法操作")
			return
		else:
			cur = self.head
			if cur.item == item:
				if cur.next == None:
					self.head = None
				else:
					cur.next.prev = None
					self.head = cur.next
				return
			while cur.next != None:
				# 直到当前节点为链表的最后一个节点
				if cur.item == item:
					cur.prev.next = cur.next
					cur.next.prev = cur.prev
					break
				cur = cur.next
			cur.prev.next = None  #将链表的最后一个节点删除


#  队列(链式队列)

class Node(object):
	def __init__(self,item, next = None):
		self.item = item
		self.next = next


class Queue(object):
	def __init__(self):
		self.head = None #队首元素
		self.rear = None #队尾元素

	def is_empty(self):
		return self.head == None
	def print_queue(self):
		cur = self.head
		myqueue = []
		while cur != None:
			myqueue.append(cur.item)
			cur = cur.next
		print(myqueue)
	def enqueue(self,item):
		# 入队
		node = Node(item)
		if self.is_empty():
			self.head = node
			self.rear = node
		else:
			self.rear.next = node
			self.rear = node
	def dequeue(self):
		# 出队
		#rtype: int(head)
		if self.is_empty():
			print("Queue is empty")
		else:
			result = self.head.item
			self.head = self.head.next
			return result
	def peek(self):
		if self.is_empty():
			print("Queue is empty")
		else:
			return self.head.item

#   队列(数组实现)

class Queue1():
	def __init__(self):
		self.value = []
		self.length = 0
		self.first = 0
	def __str__(self):
		printed = '<' + str(self.value)[1:-1] + '>'
		return printed

	def enqueue(self, value):
		self.length += 1
		self.value.append(value)

	def dequeue(self):
		result = self.value[self.first]
		self.length -= 1
		self.first += 1
		self.value = self.value[self.first:]
		return result

	def peek(self):
		return self.value[0]
	def print_queue(self):
		print(self.value)

s = Queue1()
print(s)
s.enqueue(5)
s.enqueue(6)
print(s)