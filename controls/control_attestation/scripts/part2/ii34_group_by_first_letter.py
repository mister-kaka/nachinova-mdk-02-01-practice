# Задание 34. Словари: группировка по первой букве

def group_by_first_letter(words):
    result = {}
    for word in words:
        letter = word[0]
        if letter not in result:
            result[letter] = []
        result[letter].append(word)
    return result


print(group_by_first_letter(['apple', 'banana', 'avocado', 'cherry']))
print(group_by_first_letter([]))
print(group_by_first_letter(['x']))
