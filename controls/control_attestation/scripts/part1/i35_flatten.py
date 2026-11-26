# Задание 35. Списки: сглаживание вложенного списка

def flatten(lst):
    result = []
    for x in lst:
        if type(x) == list:
            for n in x:
                result.append(n)
        else:
            result.append(x)
    return result


print(flatten([1, [2, 3], 4, [5]]))
print(flatten([[1, 2], [3, 4]]))
print(flatten([1, 2, 3]))
print(flatten([]))
