# Object Oriented Programming

- 객체 (object)
- 객체지향프로그래밍
- 클래스(Class)와 객체(object)



## 객체 (object)

> Python에서 **모든 것은 객체(object)** 이다
>
> 모든 객체는 **타입(type), 속성(attribute), 조작법(method)**을 가진다.



### 객체의 특징

- **타입(type)**: 어떤 연산자(operator)와 조작(method)이 가능한가?
- **속성(attribute)**: 어떤 상태(데이터)를 가지는가?
- **조작법(method)**: 어떤 행위(함수)를 할 수 있는가?



### 타입(Type)과 인스턴스(Instance)

| type   | instance                                 |
| ------ | ---------------------------------------- |
| `int`  | 0, 1, 2                                  |
| `str`  | '', 'hello', '1', '123'                  |
| `list` | [], ['h', 'e', 'l', 'l', 'o'], [1, 2, 3] |
| `dict` | {}, {'key' : 'value'}                    |



### Type

- 공통된 속성(attribute)과 method를 가진 객체들의 분류



### Instance

- 특정 type의 실제 데이터 예시이다.
- Python에서 모든 것은 객체이고, **모든 객체는 특정 타입의 인스턴스**이다.



### 속성(Attribute)과 메서드(Method)

> 우리가 아는 type의 attribute와 method에 대해 정리해보자



| type      | attributes       | methods                        |
| --------- | ---------------- | ------------------------------ |
| `dict`    | _                | .keys(), .values(), .items()   |
| `str`     | _                | .strip(), .split(), .isupper() |
| `list`    | _                | .append(), .extend(), .sort()  |
| `complex` | `.real`, `.imag` |                                |



### attribute

> 객체의 상태, 데이터를 뜻한다.



- `<객체>.<속성>`으로 접근할 수 있다.



```python
# 복소수의 실수부를 print 해보자

cnum = 3+4j
print(cnum.real) # -> 3.0
print(type(cnum)) # -> complex
```

```python
3.0
<class 'complex'>
```



### method

> 특정 객체에 적용할 수 있는 `행위`를 뜻한다.



- `<객체>.<method>()`를 통해 행위를 실행할 수 있다.



```python
# list를 sort시켜보자

my_list = [14, 6, 12, 7]
my_list.sort()
print(my_list)
```

```
[6, 7, 12, 14]
```



## 클래스(Class)와 객체(object)

- **type** : 공통 속성을 가진 객체들의 분류
- **class** : 객체들의 *분류를 정의* 할 때 쓰이는 키워드



### 클래스 생성

- 클래스 생성은 `class`키워드와 정의하고자 하는 `클래스의 이름`으로 가능하다.
- `클래스의 이름`은 `PascalCase`로 정의한다.
- 클래스 내부에는 데이터와 함수를 정의할 수 있고, 이때 데이터는 **attribute** 그리고 정의된 함수는 **method**로 불린다.



**활용법**

```python
class 클래스 이름:
    <statement>
```



```python
# 사람 클래스의 객체를 만들어보자
class Person:
    pass
    
jiyong = Person() # 클래스이름()을 호출함으로써 생성된다. (생성자)
print(type(jiyong))
```

```
<class '__main__.Person'>
```



### method 정의

> 특정 데이터 타입(또는 클래스)의 객체에 공통적으로 적용 가능한 행위(behavior)들을 의미한다.



**활용법**

```python
class 클래스이름:
    # method
    def my_class_method(self): # self뒤에 필요한 매개변수를 정의할 수 있다.
        print('method 호출!')
```



```python
# 말하는 사람 클래스를 선언해보자

class Person:
    
    def talk(self):
        print(f'안녕, 나는 사람이야')
        
jiyong = Person()
jiyong.talk()
```

```
안녕, 나는 사람이야
```



### self

> Instance 자신(self)



- Python에서 instance method는 **호출 시 첫번째 인자로 자기 자신이 전달**되게 설계되었다.
- 보통 매개변수명으로 `self`를 첫번째 인자로 설정한다.



```python
# 이름 속성을 가지고 print 할 수 있는 클래스를 선언하고, 그 객체를 생성한다.

class Person:
    def __init__(self, name): # 생성자
        self.name = name
    
    def talk(self):
        print(f'안녕, 내 이름은 {self.name}이야!')
        
jiyong = Person('김지용')
jiyong.talk()
```

```
안녕, 내 이름은 김지용이야!
```



### 생성자(constructor) 메서드

> instance 객체가 생성될 때 호출되는 함수



**활용법**

```python
class 클래스이름:
    def __init__(self): # 필요한 매개변수를 self뒤에 넣어줄 수 있다.
        print('생성될 때 자동으로 호출되는 method입니다.')
```



### 소멸자(destructor) 메서드

> instance 갹체가 소멸되기 직전에 호출되는 함수.



**활용법**

```python
class 클래스이름:
    def __del__(self):
        print('소멸되기 직전에 호출되는 method입니다.')
```



### 매직 method

- 더블언더스코어(`__`)가 있는 메서드는 특별한 일을 하기 위해 만들어진 메서드이기 때문에 `스페셜 메서드` 혹은 `매직 메서드`라고 불립니다.

- 매직(스페셜) 메서드 형태

  ```
  __someting__
  ```

  ```
  '__new__',
  '__reduce__',
  '__reduce_ex__',
  '__repr__',
  '__rmod__',
  '__rmul__',
  '__setattr__',
  '__sizeof__',
  '__str__',
  ```



#### `__str__(self)`

```python
# 이름 속성을 가지고 print 할 수 있는 클래스를 선언하고, 그 객체를 생성한다.
class Person:
    def __init__(self, name): # 생성자
        self.name = name
    
    def talk(self):
        print(f'안녕, 내 이름은 {self.name}이야!')
        
    def __str__(self):
        # 스트링으로 전환하면 return되는 함수 정의
        return self.name
   
    
jiyong = Person('김지용')
x = str(jiyong)
print(x) # print(jiyong)도 가능
```

