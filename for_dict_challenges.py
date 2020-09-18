from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

list_names = []
for name in students:
    list_names.append(students[students.index(name)]['first_name'])

count = Counter(list_names)

for name in count:
    print(f'{name}: {count[name]}')

print()
#for name in list(set(list_names)):
    #print(f"{name}: {list_names.count(name)}")  # Если без Counter (вывод не упорядочен)

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'}
]

list_names = []
for name in students:
    list_names.append(students[students.index(name)]['first_name'])

max_name = ''
count_name = 0
for name in list(set(list_names)):
    if list_names.count(name) > count_name:
        max_name = name
        count_name = list_names.count(name)
    elif list_names.count(name) == count_name:
        max_name = max_name + ', ' + name

print(f"Самое частое имя среди учеников: {max_name}\n")

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
]

list_names_full = []
for students in school_students:
    list_names = []
    for name in students:
        list_names.append(students[students.index(name)]['first_name'])
    list_names_full.append(list_names)

for students in list_names_full:
    max_name = ''
    count_name = 0
    for name in list(set(students)):
        if students.count(name) > count_name:
            max_name = name
            count_name = students.count(name)
        elif students.count(name) == count_name:
            max_name = max_name + ', ' + name
    print(f"Самое частое имя в классе {list_names_full.index(students) + 1}: {max_name}")
print()

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

for school_class in school:
    boys_quantity = 0
    girls_quantity = 0
    for name in school_class['students']:
        if not is_male[name['first_name']]:
            girls_quantity += 1
        else:
            boys_quantity += 1
    print(f"В классе {school_class['class']}: {girls_quantity} девочки и {boys_quantity} мальчика")

print()

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

result_girls = {"class": '', "quantity": 0}  # Словарь для хранения результата для девочек
result_boys = {"class": '', "quantity": 0}  # Словарь для хранения результата для мальчиков
for school_class in school:
    boys_quantity = 0
    girls_quantity = 0
    for name in school_class["students"]:
        if not is_male[name["first_name"]]:
            girls_quantity += 1
        else:
            boys_quantity += 1

    if girls_quantity > result_girls["quantity"]: #Если в очередном классе девочек больше, перезаписываем
        result_girls["class"] = school_class["class"]
        result_girls["quantity"] = girls_quantity
    elif girls_quantity == result_girls["quantity"]: #Если в разных классах количество равно, дозаписываем
        result_girls["class"] = result_girls["class"] + ", " + school_class["class"]

    if boys_quantity > result_boys["quantity"]:
        result_boys["class"] = school_class['class']
        result_boys["quantity"] = boys_quantity
    elif boys_quantity == result_boys["quantity"]:
        result_boys["class"] = result_boys["class"] + ", " + school_class["class"]

print(
    f"Больше всего мальчиков в классе: {result_boys['class']}\n"
    f"Больше всего девочек в классе: {result_girls['class']}")

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
