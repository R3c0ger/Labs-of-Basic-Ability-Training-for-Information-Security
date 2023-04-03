#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import math

# 题目九：两地之间距离计算

# 计算两点p1, p2之间的距离
# p1：（纬度、经度）
# p2: （纬度、经度）
def sphere_distance(p1, p2):
    pass


# 题目十：计算Fibonacci 序列的值
# Fibonacci是1，1, 2，3，5, 8，13.....
# n1 = 1, n2 =2, n3 = n1+n2, n4 = n3+n2
def fibonacci_recursion(number):
    pass

def fibonacci_loop(number):
    pass

# 题目一：水仙花数
def narcissistic_number():
    result = []
    for i in range(100, 999):
        figure = str(i)
        if int(figure[0]) ** 3 + int(figure[1]) ** 3 + int(figure[2]) ** 3 == i:
            result.append(i)
    return result

# 题目二：完美数
def perfect_number(limit=1000):
    if (limit < 1) or ( not isinstance(limit,int) ):
        return "Parameter Error."
    else:
        result = []
        for i in range(2, limit+1):
            sum = 0
            for j in range(1, i):
                if i % j == 0:
                    sum += j
            if sum == i:
                result.append(i)
    return result

# 题目三：百钱百鸡
def buy_chicken():
    result = []
    for i in range(0, 21):
        for j in range(0, 34):
            k = 100 - i - j
            if (k % 3 == 0) and (5 * i + 3 * j + k / 3 == 100):
                result.append([i, j, k])
    return result

#题目四
# 最大公约数
def gcd(x, y):
    if x < 1 or y < 1 or not isinstance(x,int) or not isinstance(y,int):
        return "Parameter Error."
    max_num = max(x, y)
    min_num = min(x, y)
    while min_num != 0:
        temp = max_num
        max_num = min_num
        min_num = temp % max_num
    return max_num

# 最小公倍数
def lcm(x, y):
    if x < 1 or y < 1 or not isinstance(x, int) or not isinstance(y, int):
        return "Parameter Error."
    return x * y // gcd(x, y)


# 题目五：回文数
def is_palindrome_number(num):
    if not isinstance(num, (int, float)):
        return False
    s = str(num)
    return s == s[::-1]

# 题目六：素数
def is_prime_num(num):
    if num < 1 or not isinstance(num, int):
        return "Parameter Error."

    if num == 1:
        return False
    elif num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# 题目七：约瑟夫环
def jose_prob(n, m):
    pass

# 题目八：万年历
def calendar(year, month, day):
    pass

if __name__ == '__main__':
    calendar(2012,7,12)
