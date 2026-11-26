# Задание 36. Множества: уникальные слова

def unique_words(text):
    result = []
    for word in text.lower().split():
        if word not in result:
            result.append(word)
    return result


print(unique_words('hello world hello python'))
print(unique_words('Python python PYTHON'))
print(unique_words(''))
