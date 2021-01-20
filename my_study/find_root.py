# 0118 과제 중 근의 공식 자료가 가장 어렵다고 판단하여 업로드 합니다~

def formula_root(lst):
    if len(lst) != 3:
        return "3개의 계수를 입력하시오."
        
    a, b, c = lst
    D = (b**2) - (4*a*c)

    if D>0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        return x1, x2
    elif D==0:
        x = -b / 2*a
        return x
    else:
        x1 = f'{-b/(2*a)}+{((abs(D))**0.5)/(2*a)}j'
        x2 = f'{-b/(2*a)}-{((abs(D))**0.5)/(2*a)}j'
        return complex(x1), complex(x2) # 복소수화
               
input_str = input("이차방정식의 각각의 계수를 순서대로 입력하시오.(예시 : 1, -2, 1) : ")
str_lst = input_str.split(', ')
num_lst = [int(i) for i in str_lst]
result = formula_root(num_lst)
print(result)
