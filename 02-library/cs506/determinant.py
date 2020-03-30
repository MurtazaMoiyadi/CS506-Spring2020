def two_by_two(matrix):
    if len(matrix[0]) != 2:
        raise ValueError("matrix must be two by two")
    det = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
    return det



def n_by_n(matrix):
    if len(matrix)==2:
        return two_by_two(matrix)
    else:
        det = 0
        for i in range(1, len(matrix)+1):
            new_matrix = [matrix[1:][:i], matrix[1:][i+1:]]
            print(new_matrix)
            rest = n_by_n(new_matrix)
            if i%2==0:
                rest = -rest
            det += (matrix[0][i-1]*rest)
        return det

print(n_by_n([[3, 3, 3], [3, 3, 3], [3, 2, 3]]))