# Задание 35. Кортежи: подсчёт статистики

def stats(students):
    if len(students) == 0:
        return (None, None, None)
    min_grade = students[0][1]
    max_grade = students[0][1]
    total = 0
    for name, grade in students:
        if grade < min_grade:
            min_grade = grade
        if grade > max_grade:
            max_grade = grade
        total += grade
    avg = round(total / len(students), 2)
    return (min_grade, max_grade, avg)


print(stats([('A', 3), ('B', 5), ('C', 4)]))
print(stats([('A', 2), ('B', 3), ('C', 4)]))
print(stats([]))
