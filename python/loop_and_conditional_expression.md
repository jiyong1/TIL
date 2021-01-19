## 조건 표현식(Conditional Expression)

- 조건 표현식은 일반적으로 조건에 따라 값을 정할 때 활용된다.
- **삼항 연산자(Ternary Operator)**라고 부르기도 한다.

------



**활용법**

```python
true_value if <조건식> else false_value
```



**절댓값 예시**

```python
num = int(input('숫자를 입력하세요 : '))
value = num if num>=0 else -num
print(value)
```

```
숫자를 입력하세요 : -5
5
```



## 반복문(Loop Statement)

- while
- for



### `while` 반복문

> `while` 문은 조건식이 참(`True`)인 경우 반복적으로 코드를 실행한다.

- `while` 문 역시 조건식 뒤에 콜론(`:`)이 반드시 필요하며, 이후 실행될 코드 블럭은 **4spaces**로 **들여쓰기**를 한다.
- **반드시 종료조건을 설정해야 한다.**

---



 **활용법**

- **문법**

```python
while <조건식>:
    <코드 블럭>
```

- 예시

```python
while True: # True 대신 조건식
    print('조건식이 참일 때까지')
    print('계속 반복')
```

```python
# 자리 수 예제
n = int(input('숫자를 입력하시오. : '))

while n>0:
    print(n%10)
    n //= 10
```

```
숫자를 입력하시오. : 185
5
8
1
```





### `for` 문

> `for` 문은 시퀀스(string, tuple, list, range)나 다른 순회가능한 객체(iterable)의 요소들을 순회한다.

------



**활용법**

- **문법**

```python
for <임시변수> in <순회가능한데이터(iterable)>:
    <코드 블럭>
```

- **예시**

```python
for menu in ['김밥', '햄버거', '피자', '라면']:
    print(menu)
```



#### enumerate

> 인덱스(index)와 값(value)을 함께 활용 가능



- `enumerate()`를 활용하면, 추가적인 변수를 활용할 수 있다.

- `enumerate()`는 내장 함수 중 하나이며, 다음과 같이 구성되어 있다.

![](loop_and_conditional_expression.assets/61180561-3993e180-a653-11e9-9558-085c9a0ad65d.png)

---



- **문법**

```python
for <변수1>, <변수2> in enumerate(순회가능한데이터(iterable), start):
    <코드 블럭>
    
# start = 0(default)
```

- **예시**

```python
lunch = ['짜장면', '초밥', '피자', '햄버거']

for idx, menu in enumerate(lunch, 1):
    print(f'{menu}는 lunch list의 {idx}번 원소입니다.')
```





## 반복제어(`break`, `continue`, `for-else`)



### `break`

> 반복문을 종료한다.

- `for` 나 `while` 문에서 빠져나간다.



```python
# break 사용 안함
n = 0
while n < 3:
    print(n)
    n += 1
```

```python
# break 사용
n = 0
while True:
    if n == 3:
        break
    print(n)
    n += 1
```

```python
# for 문
rice = ['보리', '보리', '보리', '쌀', '보리']
for i in rice:
    print(i)
    if i == '쌀':
        break
```

```
보리
보리
보리
쌀
```



### `continue`

> `continue`문은 continue 이후의 코드를 수행하지 않고 *다음 요소부터 계속(continue)하여* 반복을 수행한다.



```python
for i in range(10):
    if i%2 == 0:
        continue
    print(f'{i}는 홀수입니다.')
```

```
1는 홀수입니다.
3는 홀수입니다.
5는 홀수입니다.
7는 홀수입니다.
9는 홀수입니다.
```



### `else`

끝까지 반복문을 실행한 이후에 실행된다.

- 반복에서 리스트의 소진이나 (`for` 의 경우) 조건이 거짓이 돼서 (`while` 의 경우) 종료할 때 실행된다.
- 하지만 반복문이 **`break` 문으로 종료될 때는 실행되지 않는다.** (즉, `break`를 통해 중간에 종료되지 않은 경우만 실행)

---



- **예시**

```python
# for 예시 1
for i in range(3):
    print(i)
else:
    print('끝!')
```

```
0
1
2
끝!
```



```python
# for 예시 2
for i in range(3):
    print(i)
    if i==1:
        print('끝!')
        break
else:
    print('나는 print 안될거야')
```

```
0
1
끝!
```



```python
# while 예시
n = 0
while n < 3:
    print(n)
    n += 1
else:
    print('끝')
```

```
0
1
2
끝
```





### `pass`

>  아무것도 하지 않는다.

- 문법적으로 문장이 필요하지만, 프로그램이 특별히 할 일이 없을 때 자리를 채우는 용도로 사용할 수 있다.

---



```python
for i in range(5):
```

```
  File "<ipython-input-16-207c0a79ae82>", line 2
    for i in range(5):
                      ^
SyntaxError: unexpected EOF while parsing
```



```python
for i in range(5):
    pass

# 오류 X
```

