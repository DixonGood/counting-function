def homework(item):
    counst = {}
    for num in item:
        counst[num] = counst.get(num, 0) + 1
    return counst

numbers = [1, 7, 10, 5, 5, 9, 7, 13, 6]
counst = homework(numbers)
print(counst)

