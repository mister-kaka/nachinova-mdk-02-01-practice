# Задание 34. Списки: пересечение двух списков

def intersection(a, b):
    result = []
    for x in a:
        if x in b and x not in result:
            result.append(x)
    return result


print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))
print(intersection([1, 1, 2, 2, 3], [2, 3, 3, 4]))
print(intersection([1, 2], [3, 4]))
print(intersection([], [1, 2]))
