# 题目 1

## 题目

What is the HTML tag used to show an image?

## 解题思路

搜索即可。

另外，在 Typora 中，对已经插入到文中的 `![]()` 格式的图片设置缩放，则该行代码会自动变成 HTML 代码，例如：`<img src="img/Pasted%20image%2020230427171447.png" style="zoom:50%;" />`

综上，用于显示图像的 HTML 标签是：`<img>`

## 截图

![](img/Pasted%20image%2020230427171447.png)

# 题目 2

## 题目

What is the CSS "property: value" used to make an HTML element's text aligned to the left? 

## 解题思路

在浏览器当中按 <kbd>F12</kbd> 、在 Typora 中按 <kbd>Shift</kbd>+<kbd>F12</kbd>、在 Obsidian 中按 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> 打开开发者模式，在“查看器”的样式过滤器中输入 `align` 即可看得到 `text-align: left;` 之类的内容。

## 截图

![](img/Pasted%20image%2020230427181006.png)

# 题目 3

## 题目

Check the above login form for exposed passwords. Submit the password as the answer.

## 解题思路

查看网页源代码即可。

发现 `<!-- TODO: remove test credentials admin:HiddenInPlainSight -->`，根据 Sensitive Data Exposure 所讲授的内容和例子，我们可以推断冒号后的内容就是测试用例的密码。

## 截图

![](img/Pasted%20image%2020230427181407.png)

![](img/Pasted%20image%2020230427174028.png)

# 题目 4

## 题目

What text would be displayed on the page if we use the following payload as our input: `<a href="http://www.hackthebox.com">Click Me</a>`

## 解题思路

该载荷是一段 HTML 超链接代码，显示在页面上的文本是在开始标签 `<a>` 和结束标签 `</a>` 之间的 `Click Me`，推知最终页面呈现的文本是 `Your name is Click Me`。

在 HTB 的虚拟机中可以证实上述内容。

## 截图

![](img/Pasted%20image%2020230427183235.png)

![](img/Pasted%20image%2020230427183401.png)

![](img/Pasted%20image%2020230427182945.png)

# 题目 5

## 题目

Try to use XSS to get the cookie value in the above page

## 解题思路

教程当中已经给出弹出 cookie 的 XSS 攻击载荷，在虚拟机中输入并确认即可弹窗显示 cookie 内容。`<img src=/ onerror=alert(document.cookie)>` 表示插入图片，但图片不存在，触发 onerror 事件，弹窗显示 cookie 内容。

## 截图

![](img/Pasted%20image%2020230427184248.png)

![](img/Pasted%20image%2020230427184431.png)

![](img/Pasted%20image%2020230427184500.png)

# 题目 6

## 题目

What operating system is 'WAMP' used with?

## 解题思路

阅读教程可知，WAMP 组合由 Windows、Apache、MySQL 和 PHP 这四个后端组件‌组成，即 Windows Apache Mysql PHP 集成环境。因此 WAMP 使用的操作系统是 Windows。

## 截图

![](img/Pasted%20image%2020230427185539.png)

# 题目 7

## 题目

If a web server returns an HTTP code 201, what does it stand for?

## 解题思路

查阅 [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) 可知，201 表示 `Created`，即请求成功，创建了一个新资源。这通常是在 `POST` 请求或某些 `PUT` 请求之后发送的响应。

## 截图

![](img/Pasted%20image%2020230427190424.png)

# 题目 8

## 题目



## 解题思路



## 截图



# 题目 9

## 题目



## 解题思路



## 截图



# 题目 10

## 题目



## 解题思路



## 截图



# 题目 11

## 题目



## 解题思路



## 截图



