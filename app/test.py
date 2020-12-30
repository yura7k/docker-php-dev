# Друкє усі зарезервовані слова
'''import keyword
print(keyword.kwlist)'''

# Функція сортує список сі словників по заданому ключу "price"
"""
test = [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]

def bigger_price(limit: int, data: list) -> list:

    rez = sorted(data, key= lambda x: x['price'], reverse= True)[:limit]
    return rez """

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    if text.find(begin) >= 0:
        firstEl = text.find(begin) + len(begin)
    else:
        firstEl = 0

    if text.find(end) >= 0:
        lastEl = text.find(end)
    else:
        lastEl = len(text)

    if firstEl > lastEl:
        rez = ""
    else:
        rez = text[firstEl:lastEl]

    return rez

test = "No [b]hi"

print(between_markers(test, '[b]', '[/b]'))