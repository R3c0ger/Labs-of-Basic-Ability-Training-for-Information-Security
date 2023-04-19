#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

# 题目十一：摩斯码生成器
def morse_code(usr_str):
    # 定义初始摩斯码字典，保留摩斯码字符之间没有空格的形式，以作兼容。
    morse_dict_src = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                      'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                      'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                      'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
                      '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                      '7': '--...', '8': '---..', '9': '----.'}
    # 生成摩斯码字符之间有指定空格数量的摩斯码字典。
    morse_dict = {}
    for key in morse_dict_src:
        if key not in morse_dict:
            morse_dict[key] = ''
        for morse_char in morse_dict_src[key]:
            morse_dict[key] += (morse_char + ' ' * 1) # （1）点、破折号之间为一个空格。
        morse_dict[key] = morse_dict[key].strip() # strip()不带参数，默认清除首尾的空白符。[0:-1]也能实现这个要求。

    # 将输入字符串转为大写字母形式，遍历字符串并转换为摩斯码
    morse_code = ''
    for char in usr_str.upper():
        if char in morse_dict:
            morse_code += (morse_dict[char] + ' ' * 3) # （2）字符间为三个空格。
        elif char == ' ':
            morse_code += ' ' * (7 - 3) # （3）每个字符后都添加3个空格，因此单词后额外添加4个空格就可满足要求。
    return morse_code.strip()

# 题目十二：词频统计
def word_freq(path):
    # 读取sight word.txt文件，转换为字符串，将所有单词转为小写之后，按空字符分割成高频词列表，便于查找
    with open('./testData/sight word.txt', 'r') as file:
        sight_words = file.read().lower().split()

    # 创建一个字典，用于存入文件中的所有单词，和对应的出现次数。
    word_count = {}
    with open(path, 'r') as file:
        # 读取path文件，转换为字符串，将所有单词转为小写。
        # 使用正则表达式将file字符串中的非必要符号转换为空格。
        file = re.sub(r'[!`~@#$%^&*()_\-+=\[\]{}\/?,.:\"\\<\/>\s]', " ", file.read().lower()) # \s 表示匹配任意一个空白字符
        # 使用正则表达式对file字符串进行单词匹配，对所有查找出的字符串在高频词列表中查找，非频繁词加入字典中并计数。
        words = re.findall(r'\b[a-zA-Z\']+\b', file)
        for word in words:
            if word not in sight_words:
                word_count[word] = word_count.get(word, 0) + 1 # get()方法返回指定键的值，如果值不在字典中返回默认值0。

    # 将字典转化为二元组列表，并使用匿名函数，按次数和单词的倒序进行排序
    word_list = list(word_count.items())
    word_list.sort(key = lambda pair: (pair[1], pair[0]), reverse=True) # sorted()
    return word_list[:10]

# 题目十四：敏感词过滤
def filter_words(user_input):
    # 读取敏感词库文件，将其中的敏感词加入敏感词列表 sensitive_words 中。
    with open('./testData/sensitive.txt', 'r') as file:
        # “第x类”所在行不是敏感词，应去除同时具有“第”和“类”两个字的文本行。同时空行也不是敏感词。
        sensitive_words = [line.strip() for line in file if not re.findall(r'第.*类|^\s*$', line)]

    # 过滤敏感词
    for word in sensitive_words:
        if word in user_input:
            user_input = user_input.replace(word, '*' * len(word))
    return user_input

if __name__ == '__main__':
    li = morse_code('I love Python')
    print(li)



