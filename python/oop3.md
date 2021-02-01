# Object Oriented Programming 3

- 상속(Inheritance)
- 메서드 오버라이딩(Method Overriding)
- 다중 상속(Multiple Inheritance)



## 상속

> 클래스에서 가장 큰 특징은 `상속`이 가능하다는 것이다.
>
> 부모 클래스의 모든 속성이 자식 클래스에게 상속 되므로 코드 재사용성이 높아진다.



**활용법**

```python
class ChildClass(ParentClass):
    <code block>
```



```python
class Person: # 부모 클래스
    population = 0
    def __init__(self, name):
        self.name = name
        Person.population += 1
        
class Student(Person):
    def __init__(self, name):
        super().__init__(self, name)
        
professor = Person('김교수')
jiyong = Student('김지용')
print(Person.population)
```

```
2
```



### super()

- 자식 클래스에 메서드를 추가로 구현할 수 있다.
- 부모 클래스의 내용을 사용하고자 할 때, `super()`를 사용할 수 있다.
- 위 코드와 같이 자식 클래스 생성자에서 super()를 선언한 것을 볼 수 있다.



## 메서드 오버라이딩

> Method Overriding(메서드 재정의): 자식 클래스에서 부모 클래스의 메서드를 재정의하는 것



- 상속 받은 메서드를 `재정의`할 수도 있다.
- 상속 받은 클래스에서 **같은 이름의 메서드**로 덮어쓴다.



**예시**

```python
class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f'안녕, 난 {self.name}이야')
    
class Soldier(Person):
    def __init__(self, name, lv):
        super().__init__(name)
        self.level = lv
     
    def talk(self):
        print(f'충성! {self.level} {self.name}입니다! ^^7')
        
jiyong = Person('김지용')
soldier = Soldier('유시진', '대위')
jiyong.talk()
soldier.talk()
```

```
안녕, 난 김지용이야
충성! 대위 유시진입니다! ^^7
```



```python
class Person:
    population = 0
    
    def __init__(self, name='사람'):
        self.name = name
        Person.population += 1
        
    def talk(self):
        return f'반갑습니다. {self.name}입니다.'
    
class Student(Person): # Person의 자식 클래스
    def __init__(self, name, school):
        Person.__init__(self, name) # super()를 대신 사용해도 된다.
        self.school = school
        
    def talk(self): # Person 클래스 talk 메서드 재정의
        return Person.talk(self) + f' 저는 {self.school}에 다닙니다'
    
professor = Person('김교수')
jiyong = Student('김지용', '서울과학기술대학교')
print(Person.population)
print(professor.talk())
print(jiyong.talk())
```

```
2
반갑습니다. 김교수입니다.
반갑습니다. 김지용입니다. 저는 서울과학기술대학교에 다닙니다
```



## 다중 상속

> 두개 이상의 클래스를 상속받는 경우, 다중 상속이 된다.



**예시**

```python
# 사람 -> 아빠, 엄마 -> 자식
import random
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'안녕 나는 {self.name}이야')
class Father(Person):
    gender = '남자'
    chromosome = 'XY'
    def __init__(self, name):
        super().__init__(name)
      
class Mother(Person):
    gender = '여자'
    chromosome = 'XX'
    def __init__(self, name):
        super().__init__(name)

class Child(Father, Mother):
    def __init__(self, name):
        Person.__init__(self, name)
        self.chromosome = Mother.chromosome[random.randint(0,1)] + Father.chromosome[random.randint(0,1)]
        if self.chromosome == 'XY':
            self.gender = '남자'
        elif self.chromosome == 'XX':
            self.gender = '여자'
        else:
            self.gender = '...'
            
    def gender_print(self):
        print(f'나는 {self.chromosome}염색체를 가진 {self.gender}야')
        
jiyong = Child('지용')
jiyong.talk()
jiyong.gender_print()
```

```
안녕 나는 지용이야
나는 XY염색체를 가진 남자야
# '나는 XX염색체를 가진 여자야' 도 가능하다
```

