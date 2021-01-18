[toc]

tmi : 오늘은 컨테이너와 반복 그리고 제어문에 대해서 배웠는데 반목 및 제어문은 기존에 다룬 언어와 비슷한 로직으로 흘러가니 넘기고.. 파이썬의 컨테이너에 대해 정리하였다.



# 컨테이너(Container)

여러 개의 값을 저장할 수 있는 것(~~객체~~)

- 시퀀스(Sequence)형: 순서가 있는(ordered) 데이터
- 비 시퀀스(Non-sequence)형: 순서가 없는(unordered) 데이터



`시퀀스`는 데이터가 순서대로 나열된(ordered) 형식을 나타냅니다.

- **주의! 순서대로 나열된 것이 `정렬되었다(sorted)`라는 뜻은 아니다.**



## Sequence Container

1. 순서를 가질 수 있다.
2. **특정 위치의 데이터를 가리킬 수 있다.**



### 종류

파이썬에서 기본적인 시퀀스 타입은 다음과 같습니다.

- 리스트(list)
- 튜플(tuple)
- 레인지(range)
- *문자형(string)*



### list

![](Container.assets/61180421-fe90ae80-a650-11e9-8211-d06f87756d05.png)



**활용법**

```python
[value1, value2, value3]
```

리스트는 대괄호`[]` 및 `list()` 를 통해 만들 수 있습니다.

값에 대한 접근은 `list[i]`를 통해 합니다.



```python
# 리스트 생성
lst = [1, 2, 3,] #lst =list((1,2,3))
print(lst[1]) # 2
```



### tuple

**활용법**

```python
(value1, value2)
```

튜플은 리스트와 유사하지만, `()`로 묶어서 표현합니다.

그리고 tuple은 수정 불가능 *(불변, immutable)* 하고, 읽을 수 밖에 없습니다.

직접 사용하기 보다는 파이썬 내부에서 다양한 용도로 활용되고 있습니다.



```python
lst = (1, 2, 3,)
print(lst[1]) # 2
```



### range

`range` 는 숫자의 시퀀스를 나타내기 위해 사용됩니다.

기본형 : `range(n)`

> 0부터 n-1까지 값을 가짐

범위 지정 : `range(n, m)`

> n부터 m-1까지 값을 가짐

범위 및 스텝 지정 : `range(n, m, s)`

> n부터 m-1까지 +s만큼 증가한다



```python
type(range(3)) # range
```



### string(문자열)

> 문자열(String)이란 문자, 단어 등으로 구성된 문자들의 집합을 의미한다. 예를 들어 다음과 같은 것들이 문자열이다.

- `""`나 `''` 로 둘러싸서 표현할 수 있다.
- `"""` `'''` 로 개행문자를 포함하여 표현할 수 있다.



```python
x = 'hello python!'
print(x)

hello python!
```

```python
a = 'hello 
world' # 오류

a = '''hello
world'''
```





## Non-sequence Container

### 종류

- 셋(set)
- 딕셔너리(dictionary)



### set

`set`은 순서가 없는 자료구조입니다.

- `set`은 수학에서의 집합과 동일하게 처리된다.
- `set`은 중괄호`{}`를 통해 만들며, 순서가 없고 중복된 값이 없다.
- 빈 집합을 만들려면 `set()`을 사용해야 합니다. (`{}`로 사용 불가능.)
  - `{}`는 dictionary로 처리된다.



```python
set_a = {1, 2, 3}
print(set_a)
set_b = {3, 6, 9}
print(set_b)

{1, 2, 3}
{9, 3, 6}
```

```python
print(set_a & set_b) # 교집합 == set_a.intersection(set_b)

{3}
```





### dictionary

>  `dictionary`는 `key`와 `value`가 쌍으로 이뤄져있으며, 궁극의 자료구조이다.

![](Container.assets/61180427-1405d880-a651-11e9-94e1-1cc5c2a2ff34.png)

**활용법**

```python
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
```

- `{}`를 통해 만들며, `dict()`로 만들 수도 있다.
- `key`는 **변경 불가능(immutable)한 데이터**만 가능하다. (immutable : string, integer, float, boolean, tuple, range)
- `value`는 `list`, `dictionary`를 포함한 모든 것이 가능하다.



```python
dict_a = {}
print(type(dict_a))
dict_b = dict()
print(type(dict_b))

<class 'dict'>
<class 'dict'>
```

```python
# 지역번호(서울-02 경기-031)가 담긴 전화번호부
phone_dict = {'서울' : '02', '경기' : '031',}
print(phone_dict)
print(phone['서울'])

{'서울': '02', '경기': '031'}
02
```



## 데이터의 분류

> 데이터는 크게 변경 가능한 것(mutable)들과 변경 불가능한 것(immutable)으로 나뉘며, python은 각각을 다르게 다룬다.

`mutable` vs `immutable`



### 변경 불가능한(immutable) 데이터

- literal
  - `숫자(number)`
  - `글자(string)`
  - `참/거짓(Bool)`
- `range()`
- `tuple()`
- ~~frozenset()~~

```python
# string 원소 변경
sample = 'abc'
print(sample[0]) # 'a'

sample[0] = 'z'
TypeError: 'str' object does not support item assignment
```

```python
# immutable 데이터의 복사
num1 = 20
num2 = num1 
num2 = 10

print(num1) # 20
print(num2) # 10
```



### 변경 가능한(`mutable`) 데이터

- `list`
- `dict`
- `set`



```python
lst = [1, 2, 3, 4,]
lst[0] = 100
print(lst) # [100, 2, 3, 4]
```

```python
# mutable 데이터의 복사는 어떻게 이루어질까?
num1 = [1, 2, 3, 4,]
num2 = num1
num2[0] = 100

print(num1) # [100, 2, 3, 4]
print(num2) # [100, 2, 3, 4]
```

```python
num1 = [1, 2, 3, 4,]
num2 = num1[:]
num2[0] = 100

print(num1) # [1, 2, 3, 4]
print(num2) # [100, 2, 3, 4]
```



## 정리



![](Container.assets/61180439-44e60d80-a651-11e9-9adc-e60fa57c2165.png)