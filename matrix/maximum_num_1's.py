mat = [[1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1]]
def max_row(mat):
    index = 0
    count = -1
    for i in range(len(mat)):
        count_num = sum(mat[i])
        if count_num > count:
            count = count_num
            index = i
    print(index)
max_row(mat)                 

