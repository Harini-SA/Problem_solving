mat = [[1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1]]
def min_row(mat):
    index = 1
    count = float('inf')
    for i in range(len(mat)):
        count_num = sum(mat[i])
        if count_num < count:
            count = count_num
            index = i+1
    print(index)
min_row(mat)                 

