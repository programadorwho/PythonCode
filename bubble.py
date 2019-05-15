vector = [2, -3, 1, 0, 7, 4, -5, 9, 12, 6]
count = 0
def bubble_sort(count):
    find = True
    aux = 1
    while find:
        find = False
        for i in range(vector.__len__() - aux):
            if (vector[i] > vector[i+1]):
                print(vector)
                auxiliary = vector[i]
                vector[i] = vector[i+1]
                vector[i+1] = auxiliary
                find = True
            count+=1
        aux += 1
    return count
count = bubble_sort(count)
print(vector)
print("Number of movements: ",count)

'''@programador_who'''
