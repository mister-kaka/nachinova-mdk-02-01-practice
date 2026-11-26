# Задание 39. Комплексная задача: «Топ-3 студента»

def top_three_by_grade(students):
    top = []
    for name, grade in students:
        i = 0
        while i < len(top) and top[i][1] >= grade:
            i += 1
        if i < 3:
            top.insert(i, (name, grade))
            if len(top) > 3:
                top.pop()
    result = []
    for name, grade in top:
        result.append(name)
    return result


print(top_three_by_grade([('A', 3), ('B', 5), ('C', 4)]))
print(top_three_by_grade([('A', 5), ('B', 5), ('C', 4), ('D', 5)]))
print(top_three_by_grade([('A', 3)]))
print(top_three_by_grade([]))
