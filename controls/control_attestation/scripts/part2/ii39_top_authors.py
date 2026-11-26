# Задание 39. Комплексная задача: «Топ-N авторов по количеству книг»

def top_authors(books, n):
    counts = {}
    for title, author in books:
        if author in counts:
            counts[author] += 1
        else:
            counts[author] = 1
    pairs = []
    for author in counts:
        pairs.append([author, counts[author]])
    i = 0
    while i < len(pairs):
        j = 0
        while j < len(pairs) - 1:
            if pairs[j][1] < pairs[j + 1][1]:
                temp = pairs[j]
                pairs[j] = pairs[j + 1]
                pairs[j + 1] = temp
            elif pairs[j][1] == pairs[j + 1][1] and pairs[j][0] > pairs[j + 1][0]:
                temp = pairs[j]
                pairs[j] = pairs[j + 1]
                pairs[j + 1] = temp
            j += 1
        i += 1
    result = []
    i = 0
    while i < n and i < len(pairs):
        result.append(pairs[i][0])
        i += 1
    return result


print(top_authors([('A', 'X'), ('B', 'Y'), ('C', 'X'), ('D', 'Z'), ('E', 'X')], 2))
print(top_authors([('A', 'X'), ('B', 'Y'), ('C', 'X'), ('D', 'Y')], 2))
print(top_authors([('A', 'X')], 5))
print(top_authors([], 3))
