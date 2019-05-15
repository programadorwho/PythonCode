vectorinsert = [2, -3, 1, 0, 7, 4, -5, 9, 12, 6]
count = 0
i = 1
while i < vectorinsert.__len__():
    k = i
    while vectorinsert[k] < vectorinsert[k - 1]:
        print(vectorinsert)
        auxiliary = vectorinsert[k]
        vectorinsert[k] = vectorinsert[k-1]
        vectorinsert[k-1] = auxiliary
        count += 1
        if k > 1:
            k -= 1
    count += 1
    i += 1
print(vectorinsert)
print("Number of movements: ", count)

'''@programador_who'''
