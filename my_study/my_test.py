# 
def class_avg(students):
    try:
        return sum(students)/len(students)
    except:
        return 0

lst = []
print(class_avg(lst))
