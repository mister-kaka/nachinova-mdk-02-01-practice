# Задание 36. Списки: группировка по чётности

def group_by_parity(numbers):
    result = {'even': [], 'odd': []}
    for n in numbers:
        if n % 2 == 0:
            result['even'].append(n)
        else:
            result['odd'].append(n)
    return result


print(group_by_parity([1, 2, 3, 4, 5]))
print(group_by_parity([2, 4]))
print(group_by_parity([]))
