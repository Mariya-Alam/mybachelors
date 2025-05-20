dict = {"first":1,"second":2,"third":3}
print(dict)
dict["second"]=4
print(dict)

d2 = {'a':8,'b':5,'a':6}
print(d2)


squares = [x**2 for x in range(1,11)]
print(squares)

evens = [x for x in range(1,21) if x % 2 ==0]
print(evens)

cubes = {x : x**3 for x in range(1,6)}
print(cubes)

words = ["hello", "world"]
uppercase_words = [word.upper() for word in words]
print(words)

matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)

odd_squares = {x**2 for x in range(1,11) if x % 2 !=0}
print(odd_squares)

people = [("Awais",30),("Ali",24),("Babar",22)]
names = [name for name,age in people]
print(names)

alphabet ={chr (i): i - 96 for  i in range(97,123)}
print(alphabet)

nested_list = [[1,2],[3,4],[5]]
flat_list = [item for sublist in nested_list for item in sublist]
print(nested_list)

divisibles = [x for x in range (1,31) if x % 3 ==0 and x % 5 ==0]
print(divisibles)






students = {'std1':{'name':'ali','age':22,'courses':['math','science']},
            'std2':{'name':'Babar','age':25,'courses':['math','English']},
            'std3':{'name':'Jamal','age':26,'courses':['Art','science']}}

for student_id, info in students.items():
    print(f"{student_id}:")
    print(f"Name:{info['name']}")
    print(f"Age:{info['age']}")
    print(f"Courses:{','.join(info['courses'])}")

for student_id in students:
    print(f"{student_id}:")
    print(f"Name:{students[student_id]['name']}")
    print(f"Age:{students[student_id]['age']}")
    print(f"Courses:{','.join(students[student_id]['courses'])}")