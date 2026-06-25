def rotate(matrix):
    for i in range(len(matrix)-1):
        for j in range(i+1,len(matrix[0])):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]     

    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))