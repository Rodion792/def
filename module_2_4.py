def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        empty_list = []
        for j in range(m):
            empty_list.append(value)
            matrix.append(empty_list)
    return matrix
result1 = get_matrix(7, 2, 72)
result2 = get_matrix(3, 2, 93)
result3 = get_matrix(9, 2, 15)
print(result1)
print(result2)
print(result3)