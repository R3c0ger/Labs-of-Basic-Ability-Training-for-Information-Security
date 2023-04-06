#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import math

# 题目九：两地之间距离计算

# 计算两点p1, p2之间的距离
# p1：（纬度、经度）
# p2: （纬度、经度）
def sphere_distance(p1, p2):
    if not isinstance(p1, tuple) or not isinstance(p2, tuple) or not 0 < p1[0] < 90 or not 0 < p1[1] < 180 or not 0 < p2[0] < 90 or not 0 < p2[1] < 180:
        return "Parameter Error."
    elif not isinstance(p1[0], float) or not isinstance(p1[1], float) or not isinstance(p2[0], float) or not isinstance(p2[1], float):
        return "Parameter Error."

    phi1 = math.radians(p1[0])
    phi2 = math.radians(p2[0])
    lambda1 = math.radians(p1[1])
    lambda2 = math.radians(p2[1])
    r = 6371
    d = 2 * r * math.asin(math.sqrt(pow(math.sin(abs(phi2 - phi1) / 2), 2) + math.cos(phi1) * math.cos(phi2) * pow(math.sin(abs(lambda2 - lambda1) / 2), 2)))
    return round(d, 2)


# 题目十：计算Fibonacci 序列的值
# Fibonacci是1，1, 2，3，5, 8，13.....
# n1 = 1, n2 =2, n3 = n1+n2, n4 = n3+n2
def fibonacci_recursion(number):
    if not isinstance(number, int) or number < 1:
        return 'Parameter Error.'
    if number == 1 or number == 2:
        return 1
    else:
        return fibonacci_recursion(number - 2) + fibonacci_recursion(number - 1)

def fibonacci_loop(number):
    if not isinstance(number, int) or number < 1:
        return 'Parameter Error.'
    if number == 1 or number == 2:
        return 1
    else:
        addend1 = 1 # 前一个加数，即倒数第三项
        addend2 = 1 # 后一个加数，即倒数第二项
        # 计算第n项需要循环n-2次
        for i in range(number - 2):
            sum = addend1 + addend2
            addend1 = addend2
            addend2 = sum
        return sum

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
    if n >= m or n <= 0 or m <= 0 or not isinstance(n, int) or not isinstance(m, int):
        return "Parameter Error."

    # 建立初始的队伍列表，假设所有人都是基督徒
    queue = [1 for i in range(1, m + 1)]
    # 建立队伍列表所对应的偏移量列表
    queue_index = [j for j in range(m)]

    step = 9  # 被投海者所报的数，即步长
    cnt = 0  # 报数者在队伍中的位置，初始值为0
    for k in range(m - n):
        cnt = (cnt + step - 1) % len(queue_index)
        queue[queue_index.pop(cnt)] = 0
    return queue

# 题目八：万年历
def calendar(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        return "Parameter Error."
    elif year < 1000 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return "Parameter Error."
    elif (month == 4 and day > 30) or (month == 6 and day > 30) or (month == 9 and day > 30) or (
            month == 11 and day > 30):
        return "Parameter Error."

    days_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_past_month = 0
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days_each_month[1] = 29  # 如果是闰年，二月天数需修改
    if month == 2 and day > days_each_month[1]:
        return "Parameter Error."
    for i in range(month - 1):
        days_past_month += days_each_month[i]
    return days_past_month + day

if __name__ == '__main__':
    calendar(2012,7,12)
