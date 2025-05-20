#Question no 1
students = ['Ali', 'Babar', 'Summit', 'Rohit', 'Rui Xi', 'Zhang', 'Ahmed']

students.append('Parvais')
print(students)

students.insert(3, 'Kamran')
print( students)

students.remove('Zhang')
print(students)

rohit_index = students.index('Rohit')
print( rohit_index)

students.sort()
print( students)

students_copy = students.copy()
students_copy = students_copy[:-2]
print( students_copy)

long_names = sum(1 for name in students if len(name) > 4)
print( long_names)



#Question no 2

grades = {
    'Ali': 85,
    'Babar': 72,
    'Rohit': 90,
    'Ahmed': 99,
    'Summit': 88,
    'Chistian': 66
}

grades['Frank'] = 79
print(grades)

grades['Ali'] = 87
print(grades)

grades.pop('Ahmed')
print(grades)

print("Students:", list(grades.keys()))
print(grades)

print("Grades:", list(grades.values()))
print(grades)

print("grades >= 80:")
for name, grade in grades.items():
    if grade >= 80:
        print(f"{name}: {grade}")


average = sum(grades.values()) / len(grades)
print("avg grade:", round(average, 2))



# question no 3

math_students = {'Ali', 'Babar', 'Summit', 'Dawood'}
physics_students = {'Zhang', 'Dawood', 'Ahmed', 'Rui Xi', 'Ali'}

both_courses = math_students & physics_students
print(both_courses)

either_course = math_students | physics_students
print(either_course)

only_math = math_students - physics_students
print(only_math)

math_students.add('Mustafa')
print(math_students)

math_students.remove('Babar')
print(math_students)

is_ali_in_math = 'Ali' in math_students
print(is_ali_in_math)

all_students = math_students | physics_students
print(all_students)


#Question no 4
students_records = [
    ('Ali',20,'Computer Science'),
    ('Babar',21,'Physics'),
    ('Zhang',19,'Mathmetics'),
    ('Ahmed',22,'Engineering')
]

students_records.append(('Eve',20,'Biology'))
print(students_records)

Ali_age = next(s[1] for s in students_records if s[0] == 'Ali')
print(Ali_age)

students_names = [s[0] for s in students_records]
print(students_names)

older_than_20 = [s[0] for s in students_records if s[1] > 20]
print(older_than_20)

cs_count = sum(1 for s in students_records if s[2] == 'Computer Science')
print(cs_count)

students_records.sort(key=lambda x: x[1])
print(students_records)

oldest = max(students_records, key=lambda x: x[1])[0]
print(oldest)

# question no 5

students = {
    'Ali': {'age': 20, 'courses': ['Math', 'Physics'], 'grade': 'A'},
    'Babar': {'age': 21, 'courses': ['Chemistry', 'Biology'], 'grade': 'B'},
    'Ahmed': {'age': 30, 'courses': ['Computer Science'], 'grade': 'A+'}
}

students['Ali']['courses'].append('English')
print(students)

students['Babar']['grade'] = 'B+'
print(students)

students['Dilam'] = {'age': 20, 'courses': ['Art', 'History'], 'grade': 'A'}
print(students)

high_achievers = [name for name, info in students.items() if info['grade'] in ['A', 'A+']]
print(high_achievers)

unique_courses = set(course for info in students.values() for course in info['courses'])
print(unique_courses)

avg_age = sum(info['age'] for info in students.values()) / len(students)
print(avg_age)

multi_course_students = [name for name, info in students.items() if len(info['courses']) > 1]
print(multi_course_students)


# question no 6

student_data = [
    {'name': 'Ali', 'scores': [85, 90, 88]},
    {'name': 'Babar', 'scores': [72, 68, 75]},
    {'name': 'Ahmed', 'scores': [90, 92, 95]},
    {'name': 'Dawood', 'scores': [68, 70, 72]}
]

for std in student_data:
    std['avg'] = sum(std['scores']) / len(std['scores'])
print(student_data)

high_avg_student = max(student_data, key=lambda x: x['avg'])
print(high_avg_student)

high_achvr = [std['name'] for std in student_data if std['avg'] >= 80]
print(high_achvr)

max_score = max(score for std in student_data for score in std['scores'])
print(max_score)

for std in student_data:
    if std['name'] == 'Babar':
        std['scores'] = [score + 5 for score in std['scores']]
        std['avg'] = sum(std['scores']) / len(std['scores'])
print(student_data)

sorted_students = sorted(student_data, key=lambda x: x['avg'], reverse=True)
print(sorted_students)