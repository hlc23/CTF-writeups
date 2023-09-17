# Python101
## 11的51次方
### solution
```python
print(pow(11, 51))
```
## FOR your summation
> 由六個數字：1、2、3、4、5、6所組成的互不相同且無重複數字的三位元數字,其總合為多少?
### solution
```python
print(sum([int(str(i)+str(j)+str(k)) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7) if i != j and j != k and i != k]))
```
## IF 潤年
> 請問2000年10月23日是該年的第幾天?  
更廣義的問題是輸入某年某月某日，判斷這一天是這一年的第幾天!

### solution
```python
import datetime
print(datetime.datetime(2000, 10, 23).timetuple().tm_yday)
```

## IF幸福企業的獎金制度
> IF幸福企業的獎金制度:  
IF幸福企業發放的獎金發放是根據所得利潤來提撥。
<br></br>
當利潤  
    (I)低於或等於100萬元時，獎金可提10%；
    (2)利潤高於100萬元，低於200萬元時，低於100萬元的部分按10%提成，高於100萬元的部分，可提成7%；  
    (3)200萬到400萬之間時，高於200萬元的部分，可提成5%；  
    (4)400萬到600萬之間時高於400萬元的部分，可提成4%；  
    (5)600萬到1000萬之間時，高於600萬元的部分，可提成2%;  
    (5)1000萬 以上時，高於1000萬元的部分，可提成1%。  
小名的年度績效為2,245,678元,請問他的獎金為多少?  
(精確到整數即可:小數點部分採四捨五入)  
註:你可以設計出自由輸入任何績效的獎金計算之python程式

### solution
```python
money = 2245678
bonus = 0
if money <= 1e6:
    bonus = money * 0.1
elif 1e6 < money <= 2e6:
    bonus = 1e6 * 0.1 + (money - 1e6) * 0.07
elif 2e6 < money <= 4e6:
    bonus = 1e6 * 0.1 + 1e6 * 0.07 + (money - 2e6) * 0.05
print(round(bonus))
```

## 16進位制的計算
> 10進位的3456093847523457890 對應到16進位的值是? 請將答案塞到BreakallCTF{答案}  
上網看看python內建函數hex()的用法
### solution
```python
print(hex(3456093847523457890).replace("0x", ""))
```

## 字串的逆向工程
> Reverse String 字串的逆向工程 將底下字串esrevEergnirTsroFtsetelpmisAsisihT  
倒著寫 並把結果放入BreakallCTF{答案}
### solution
```python
print("esrevEergnirTsroFtsetelpmisAsisihT"[::-1])
```
## 黃金比例與費氏數列
> Fibonacci sequence又稱黃金分割數列是這樣一個數列：0、1、1、2、3、5、8、13、21、34、……。  
在數學上，Fibonacci sequence是以遞迴的方法來定義：  
F[0] = 0 (n=0)  
F[1] = 1 (n=1)  
F[n] = F[n-1]+ F[n-2] (n=>2)  
請問F[41]是多少?  
PS:你必須要會用遞迴函數的設計方式,但是執行效率比較好的是使用iterative(也就使用loop直接計算),這個演算法複雜度計算就留待你大學時再學習.

### solution
```python
def fib(n):
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
print(fib(41))
```

## 8進位的閱讀
> 8進位的111111111011111111111101111111111111111111111111 對應到10進位的值是? 請將答案塞到BreakallCTF{答案}
### solution
```python
print(int("111111111011111111111101111111111111111111111111", 8))
```
## 函數的虛擬碼實作
> 有一個XXX函數的虛擬碼如下：  
    
    function XXX(m, n)
        while m ≠ 0
            if n = 0
                n := 1
            else
                n := XXX(m, n-1)
            m := m - 1
        return n+1
請問XXX(2,2)的值是多少?

## solution
```python
def XXX(m, n):
    while m != 0:
        if n == 0:
            n = 1
        else:
            n = XXX(m, n-1)
        m = m - 1
    return n+1
print(XXX(2, 2))
```