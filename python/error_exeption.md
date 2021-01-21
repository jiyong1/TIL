# 에러 & 예외 처리



## 에러(error)

> 발생할 수 있는 에러의 종류를 확인해보자



### 문법 에러(Syntax Error)

> 문법 에러가 있는 프로그램은 실행되지 않는다



- 에러 발생 시 `SyntaxError`라는 키워드와 함께, 에러의 상세 내용을 보여줍니다.

- `파일이름`과 `줄번호`, `^` 문자를 통해 파이썬이 코드를 읽어 들일 때(`parser`) 문제가 발생한 위치를 표현합니다.

- `parser` 는 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 작은 '화살표(`^`)'를 표시합니다.



```python
if True:
    print('참')
else # : 를 넣지 않음
    print('거짓')
```

```
File "<ipython-input-2-cd2300dfe57f>", line 3
    else # : 를 넣지 않음
         ^
SyntaxError: invalid syntax --> SyntaxError !!
```

---





## 예외(Exception)

> 실행 도중 예상하지 못한 상황(exception)을 맞이하면, 프로그램 실행을 멈춥니다.



- 문법적으로는 옳지만, 실행시 발생하는 에러입니다.

- *아래 제시된 모든 에러는 `Exception`을 상속받아 이뤄진다.*



### ZeroDivisionError

> 0으로 나눌 수 없다.

```python
10 * (1/0)
```

```
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-3-09140a8818e2> in <module>
      1 # 0으로 나눌수는 없습니다.
----> 2 10 * (1/0)

ZeroDivisionError: division by zero
```

---





### TypeError



```python
1 + '1'
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-166aa1c716a5> in <module>
      1 # 자료형에 대한 타입 자체가 잘못 되었을 경우
----> 2 1 + '1'

TypeError: unsupported operand type(s) for +: 'int' and 'str'
```



```python
# 함수 호출 과정에서 TypeError
round('3.5')
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-dd9be65982e2> in <module>
      1 # 함수 호출 과정에서 TypeError
----> 2 round('3.5')

TypeError: type str doesn't define __round__ method
```



```python
# 필수 argument 누락
import random
random.sample([1, 2, 3])
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-bd3b8e501c1b> in <module>
      1 import random
----> 2 random.sample([1, 2, 3])

TypeError: sample() missing 1 required positional argument: 'k'
```



```python
# argument 개수 초과
random.choice([1, 2, 3], 6)
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-7-a5629217118f> in <module>
----> 1 random.choice([1, 2, 3], 6)

TypeError: choice() takes 2 positional arguments but 3 were given
```

---





### ValueError

```python
# string -> float -> int 로 바꿔주길 기대하지말자..
int('3.5')
```

```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-c4d854cc813b> in <module>
      1 # string -> float -> int 로 바꿔주길 기대하지말자..
----> 2 int('3.5')

ValueError: invalid literal for int() with base 10: '3.5'
```



```python
# 존재하지 않는 숫자를 찾고자 한다 
numbers = [1, 2]
numbers.index(3)
```

```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-10-5a60a95a65c0> in <module>
      1 # 존재하지 않는 숫자를 찾고자 한다
      2 numbers = [1, 2]
----> 3 numbers.index(3)

ValueError: 3 is not in list
```

---





### IndexError

```python
# 존재하지 않는 index로 접근 !
empty_list = []
empty_list[1]
```

```
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-11-c0f998a72552> in <module>
      1 # 존재하지 않는 index로 조회할 경우
      2 empty_list = []
----> 3 empty_list[1]

IndexError: list index out of range
```

---



### KeyError



```python
# dictionary에서 Key가 없는 경우 
songs = {'sia': 'candy cane lane'}
songs['queen']
```

```
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-12-fb506014f16e> in <module>
      1 # 딕셔너리에서 Key가 없는 경우
      2 songs = {'sia': 'candy cane lane'}
----> 3 songs['queen']

KeyError: 'queen'
```

---





### ModuleNotFoundError

```python
# 모듈을 찾을 수 없는 경우
import jiyong
```

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-13-e6078a6c7495> in <module>
----> 1 import jiyong

ModuleNotFoundError: No module named 'jiyong'
```



### ImportError

```python
# 모듈을 찾았으나 가져오는 과정에서 실패하는 경우 (존재하지 않는 클래스/함수 호출)
from random import sampl
```

```
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-15-9c395f6f4684> in <module>
      1 # 모듈을 찾았으나 가져오는 과정에서 실패하는 경우 (존재하지 않는 클래스/함수 호출)
----> 2 from random import sampl

ImportError: cannot import name 'sampl' from 'random' 
```



### KeyboardInterrupt

```python
while True:
    continue 
# ctrl+c를 통해 종료해보자
```

```
Traceback (most recent call last):
  File "c:/Users/KIM/Desktop/ssafy/TIL/my_study/my_test.py", line 2, in <module>
    continue
KeyboardInterrupt
```



## 예외 처리(Exception Handling)



### try & except

> 기본적인 예외처리 방법, `try`문을 이용하여 예외처리 할 수 있다.



- 기초 문법

```python
try:
    <코드 블럭 1>
except (예외):
    <코드 블럭 2>
```



- `try` 아래의 코드블락(code block)이 실행된다.
- 예외가 발생되지 않으면, **`except`없이 실행이 종료 된다.**
- 예외가 발생하면, **남은 부분을 수행하지 않고**, `except`가 실행된다.



```python
try:
    num = input('값을 입력하시오 : ')
    print(int(num))
except ValueError:
    print('숫자 입력하라고!!')
```

```python
try:
    empty_list = []
    print(empty_list[-1])
except IndexError as err: # 변수처럼
    print(f'{err}, 오류가 발생했습니다.')
```



#### 복수의 예외처리

- **활용법**

```python
try:
    <코드 블럭 1>
except (예외1, 예외2):
    <코드 블럭 2>
```

```python
try:
    <코드 블럭 1>
except 예외1:
    <코드 블럭 2>
except 예외2:
    <코드 블럭 3>
```



- **예시**

```python
try : 
    num = input('100으로 나눌 값을 입력하시오 : ')
    print(100/int(num))
except ZeroDivisionError:
    print("0으로 어떻게 나누니?")
except ValueError:
    print("이걸 어떻게 숫자로 바꾸니?")
```

```
100으로 나눌 값을 입력하시오 : -
이걸 어떻게 숫자로 바꾸니?
```

```
100으로 나눌 값을 입력하시오 : 0
0으로 어떻게 나누니?
```



#### else

- 에러가 발생하지 않는 경우 수행되는 문장은 `else`를 이용한다.
- 모든 except 절 뒤에와야 한다.
- try 절이 예외를 일으키지 않을 때 실행되어야만 하는 코드에 적절하다.



- **활용법**

```python
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
else:
    <코드 블럭 3>
```



- **예시**

```python
try:
    num = input('100으로 나눌 값을 입력하시오 : ')
    print(100/int(num))
except ZeroDivisionError:
    print("0으로 어떻게 나누니?")
except ValueError:
    print("이걸 어떻게 숫자로 바꾸니?")
else:
    print("똑바로 입력해줘서 고마워ㅎㅎ")
```

```
100으로 나눌 값을 입력하시오 : 5
20.0
똑바로 입력해줘서 고마워ㅎㅎ
```

```
100으로 나눌 값을 입력하시오 : jiyong
이걸 어떻게 숫자로 바꾸니?
```



#### finally

- 반드시 수행해야하는 문장은 `finally`를 활용한다.
- 즉, 모든 상황에 실행되어야만 하는 코드를 정의하는데 활용한다.
- 예외의 발생 여부과 관계없이 try 문을 떠날 때 항상 실행한다.



- **활용법**

```python
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
finally:
    <코드 블럭 3>
```





- **예시**

```python
try:
    num = input('100으로 나눌 값을 입력하시오 : ')
    print(100/int(num))
except ZeroDivisionError:
    print("0으로 어떻게 나누니?")
except ValueError:
    print("이걸 어떻게 숫자로 바꾸니?")
except:
    print('무슨 에러지.. 파악하시면 연락주세요~')
else:
    print("똑바로 입력해줘서 고마워ㅎㅎ")
finally:
    print("저는 이만 떠나겠습니다~")
```

```
100으로 나눌 값을 입력하시오 : s3
이걸 어떻게 숫자로 바꾸니?
저는 이만 떠나겠습니다~
```

```
100으로 나눌 값을 입력하시오 : 15
6.666666666666667
똑바로 입력해줘서 고마워ㅎㅎ
저는 이만 떠나겠습니다~
```





#### 예외 발생 시키기(Exception Raising)

**`raise`**를 통해 예외를 강제로 발생시킬 수 있습니다.



- **활용법**

```python
raise <에러>('메시지')
```



- **예시**

```python
def avg(scores):
    if len(scores) == 0:
        raise ValueError('학생이 없습니다.')
    else:
        return round(sum(scores)/len(scores), 2)
    
avg(9)
```



