#coding:utf-8
import time

#v1:效率非常慢 存在大量重复计算
def fib(n):
    if n==1 or n==0:
        return 1
    else:
        return fib(n-2)+fib(n-1)

#v2:增加一个中间变量缓存计算的结果

def fib2(n):
    count = 0
    if n==1 or n==0:
        count=1
    else:
        count = fib2(n-2)+fib2(n-1)
        print(count)

    return count

#v3 接着演变，我们现在构造一个缓冲区cache
#我们查表，比如用字典来保存，比如cache[8]=34,
# 我们只需要查一下8是不是在字典里面就可以了，
# 在的话直接取，不在的话再去用算法计算，是不是很爽

def fib3(n,cache=None):
    if cache is None:
        cache={}
    if n in cache:
        return cache[n]
    if n==1 or n==0:
        return 1
    else:
        cache[n]=fib3(n-2,cache)+fib3(n-1,cache)
    return cache[n]

start = time.time()
print([fib3(1000) for n in range(40)])
end = time.time()
print(end-start)
















