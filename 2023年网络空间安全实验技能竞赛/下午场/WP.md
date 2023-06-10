# Write Up

Recogerous 2023/6/9



## 签到

在公众号中发送 `flag` ，得到 flag: `flag{p1a7_a0d_vvin}`

![](img/Pasted%20image%2020230609141320.png)



## rot13

由题意可知，该字符串 `1Ebbg8Vf7Abg3Nyybjrq` 是 ROT13 加密方式。

使用工具解密，得到 flag:  `flag{1Root8Is7Not3Allowed}`

![](img/Pasted%20image%2020230609141510.png)



## 山岚

“山岚”谐音“栅栏”，再根据给出的字符串的特征（有大括号、包含 `f`、`l`、`a`、`g` 这几个字母），可以推知是栅栏加密。

使用工具解密，得到 flag: `flag{6cb9c256-5fac-4b47-a1ec-59988ff9c8d5}`

![](img/Pasted%20image%2020230609142021.png)



## base

附件中的字符串为：`4C4A575851324332474E324759544B484A555A453656325250464D58534D42544C4656454B4D534D4B524954455453554C4632453656324A4F354855474D4C4B4A563547574D43324E564A475154544B4E4E33553436534B48453D3D3D3D3D3D`

检查发现后面跟随多个 `3D`，猜测是 base 编码后的 `=` 等于号。使用工具直球地解码，得到：`LJWXQ2C2GN2GYTKHJUZE6V2RPFMXSMBTLFVEKMSMKRITETSULF2E6V2JO5HUGMLKJV5GWMC2NVJGQTTKNN3U46SKHE======`，形式很像 base 编码，猜测正确。

![](img/Pasted%20image%2020230609164637.png)

再对该字符串进行 base 家族的解码，得到 ： `ZmxhZ3tlMGM2OWQyYy03YjE2LTQ2NTYtOWIwOC1jMzk0ZmRhNjkwNzJ9`。据此猜测可能是多重加密。

![](img/Pasted%20image%2020230609164802.png)

再进行解码，发现可以得到 flag： `flag{e0c69d2c-7b16-4656-9b08-c394fda69072}`

![](img/Pasted%20image%2020230609164854.png)



## 维吉尼亚

可以确认是维吉尼亚密码，其中密文是 `lvbcfstfly`，密钥未知。

提示为 `{34 18 25 13 36 13 14 13 vghn 0ol 12wa qwsz lkjn}`，可以很容易判断后半部分 `vghn 0ol 12wa qwsz lkjn` 是使用字母和数字将明文字母圈出来的键盘密码，因此猜测前半部分同样也是一种键盘密码。由于在这些二位数字中，第一位只有 1、2、3，所以判断是坐标法。由 `18` 知，第一行是 QWERTY 所在行。

![](img/Pasted%20image%2020230609165633.png)

对提示进行解码，得到 `VIGENEREBPQAM`，前一半 `VIGENERE` 即是维吉尼亚。

使用在线工具[维吉尼亚密码加密/解密](http://www.atoolbox.net/Tool.php?Id=856)，令密钥为 `VIGENEREBPQAM`，解码得到 `qnvysocbkj`，然而上交 flag 发现这是错误的 flag。

只保留无意义的后一半部分 `BPQAM` 作为密钥，解码得到 `kglctreplm`，尝试发现这是正确的明文内容。

![](img/Pasted%20image%2020230609170328.png)

因此，flag 为：`flag{kglctreplm}`



## Rsa Roll

观察 data 文件内容，易推知附件中 `{920139713,19}` 为公钥 `{n,e}`，后面的数字是用私钥 `{d, e}` 加密的拆分开来的密文 c，需要我们根据上述信息求出明文 m。

编写解密脚本：

```python
import math  
# 公钥和密文数据  
n = 920139713  
e = 19  
ciphertext = [704796792, 752211152, 274704164, 18414022, 368270835, 483295235, 263072905, 459788476, 483295235, 459788476, 663551792, 475206804, 459788476, 428313374, 475206804, 459788476, 425392137, 704796792, 458265677, 341524652, 483295235, 534149509, 425392137, 428313374, 425392137, 341524652, 458265677, 263072905, 483295235, 828509797, 341524652, 425392137, 475206804, 428313374, 483295235, 475206804, 459788476, 306220148]  

# 求p,q  
p = 0  
q = 0  
for i in range(2, int(math.sqrt(n)) + 1):  
    if n % i == 0:  
        p = i  
        q = int(n / i)  
        break
  
# 求f(n)  
f = (p - 1) * (q - 1)
  
# 求d  
d = 0  
for i in range(1, n):  
    if (e * i) % f == 1:  
        d = i  
        break
  
# 解密  
plaintext = ""  
for i in ciphertext:  
    plaintext += chr(pow(int(i),d,n))  
print("plaintext = ", plaintext)
```

![](img/Pasted%20image%2020230609180326.png)

得到 flag：`flag{13212je2ue28fy71w8u87y31r78eu1e2}`



## miao~

使用 nc 建立连接：`nc 10.81.2.235 11055`，跟随其流程进行下去，直到让我们自己去寻找 flag。尝试使用 `ls` 命令找出 `flag` 文件，再查看该文件即可。

![](img/Pasted%20image%2020230609194442.png)

得到 flag：`flag{cf926971-2353-404b-b3a8-3273756eef4d}`
