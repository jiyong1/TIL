# Object Oriented Programming 2

- 인스턴스 & 클래스 변수
- 인스턴스 & 클래스간의 이름공간
- 인스턴스 & 클래스 메서드(+ 스태틱 메서드)



## 인스턴스 & 클래스 변수



### 인스턴스 변수

- 인스턴스의 속성(attribute)
- 각 인스턴스들의 고유한 변수
- 메서드 정의에서 `self.변수명`로 정의
- 인스턴스가 생성된 이후 `인스턴스.변수명`로 접근 및 할당



**활용법**

```python
class Person:
    def __init__(self, name):    # 인스턴스 메서드 (생성자) 
        self.name = name         # 인스턴스 변수
```



### 클래스 변수

- 클래스의 속성(attribute)
- 모든 인스턴스가 공유
- 클래스 선언 내부에서 정의
- `클래스.변수명`으로 접근 및 할당



**활용법**

```python
class Person:
    species = 'human'

print(Person.species)
```



## 인스턴스 & 클래스간의 이름공간

- **이름공간 탐색 순서**

  - 클래스를 정의하면, 클래스가 생성됨과 동시에 이름 공간(namespace)이 생성된다.

  - 인스턴스를 만들게 되면, 인스턴스 객체가 생성되고 해당되는 이름 공간이 생성된다.

  - 인스턴스의 어트리뷰트가 변경되면, 변경된 데이터를 인스턴스 객체 이름 공간에 저장한다.

  - 즉, 인스턴스에서 특정한 어트리뷰트에 접근하게 되면 **인스턴스 => 클래스** 순으로 탐색을 한다.



```python
# 클래스 변수와 인스턴스 변수
class Person:
    name = 'unknown'
    
    def talk(self):
        print(self.name)
        
jiyong = Person()
jiyong.talk()
jiyong.name = '김지용'
jiyong.talk()
```

```
unknown
김지용
```



## method의 종류



### 인스턴스 메서드 (Instance method)

- 인스턴스가 사용할 메서드
- 클래스 내부에 정의되는 메서드의 기본값은 인스턴스 메서드
- **호출시, 첫번째 인자로 인스턴스 자기자신 `self`이 전달됨**



**활용법**

```python
class MyClass:
    def instance_method(self, arg1, arg2, ...):
        ...
```



### 클래스 메서드 (Class method)

- 클래스가 사용할 메서드
- `@classmethod` 데코레이터를 사용하여 정의
- **호출시, 첫 번째 인자로 클래스 `cls`가 전달됨**



**활용법**

```python
class MyClass:
    @classmethod
    def class_method(cls, arg1, arg2, ...):
        ...
```



### 스태틱 메서드 (static method)

- 클래스가 사용할 메서드
- `@staticmethod` 데코레이터를 사용하여 정의
- **호출시, 어떠한 인자도 전달되지 않음**



**활용법**

```python
class MyClass:
    @staticmethod
    def static_method(arg1, arg2, ...):
        ...
```