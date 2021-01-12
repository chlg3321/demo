#coding:utf-8
import time


#装饰器就是将功能函数,放在另一个函数里,以增加函数本身的功能

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

# start = time.time()
# print([fib3(n) for n in range(10)])
# end = time.time()
# print(end-start)

#v4 装饰器
def decorate(func):
    cache={}
    def wrap(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrap

@decorate
def fib4(n):
    if n==1 or n==0:
        return 1
    else:
        return fib4(n-2)+fib4(n-1)

print([fib4(n) for n in range(10)])


#若不使用@decorate,等价于

def decorate(func):
    cache={}
    def wrap(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrap

# @decorate
def fib4(n):
    if n==1 or n==0:
        return 1
    else:
        return fib4(n-2)+fib4(n-1)

fib4 = decorate(fib4)
# fib4()
print([fib4(n) for n in range(10)])




# another example
'''
def is_prime(num):
    if num<2:
        return False
    elif num ==2:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True

def prime_nums():
    t1 = time.time()
    for i in range(2,10000):
        if is_prime(i):
            print(i)
    t2 = time.time()
    print(t2-t1)

prime_nums()
'''




def outer(func):
    def inner():
        print("记录日志开始")
        func() # 业务函数
        print("记录日志结束")
    return inner

def foo():
    print("foo")

foo = outer(foo) #outer函数返回的是函数名,还没有对函数进行调用
foo()
# https://zhuanlan.zhihu.com/p/27449649
# 我没有修改 foo 函数里面的任何逻辑，只是给 foo 变量重新赋值了，指向了一个新的函数对象。最后调用 foo()，不仅能打印日志，业务逻辑也执行完了。现在来分析一下它的执行流程。
# 这里的 outer 函数其实就是一个装饰器，装饰器是一个带有函数作为参数并返回一个新函数的闭包，本质上装饰器也是函数。outer 函数的返回值是 inner 函数，在 inner 函数中，除了执行日志操作，还有业务代码，该函数重新赋值给 foo 变量后，调用 foo() 就相当于调用 inner()












