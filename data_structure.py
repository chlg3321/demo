import heapq

# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p05_implement_a_priority_queue.html

'''
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
'''

#堆排序
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['shares'])
# expensive = heapq.nlargest(3, portfolio, key=lambda s: s['shares'])
# print(cheap)
# print(expensive)

# 1.5 实现一个优先级队列
class PriorityQueue:
    def __init__(self):
        self._queue=[]
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue,(-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


#1.6字典中的键映射多个值
from collections import defaultdict

# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)
# print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
# print(type(d))
# print(d[1])

#1.7 字典排序  在迭代操作的时候它会保持元素被插入时的顺序
#需要注意的是，一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
# for key in d:
#     print(key, d[key])

#1.8 字典的运算
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price =zip(prices.values(), prices.keys())
# print(list(zip(*min_price)))

# min_price is (10.75, 'FB')
# max_price = max(zip(prices.values(), prices.keys()))
# # max_price is (612.78, 'AAPL')

# print(max_price)

#1.9 查找两字典的相同点
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

print(a.keys() & b.keys()) # { 'x', 'y' }
# Find keys in a that are not in b
print(a.keys() - b.keys()) # { 'z' }
# Find (key,value) pairs in common
print(a.items() & b.items()) # { ('y', 2) }