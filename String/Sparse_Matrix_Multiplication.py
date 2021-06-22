# Write a function that takes in two integer matrices and multiplies them 
# together. Both matrices will be sparse, meaning that most of their elements will 
# be zero. Take advantage of that to reduce the number of total computations 
# that your function performs. If the matrices can't be multiplied together, your 
# function should return [[]].

# Sample Input:
# matrix_a = [
#     [0, 2, 0],
#     [0, -3, 5],
#     ]
# matrix_b = [
#     [0, 10, 0],
#     [0, 0, 0],
#     [0, 0, 4],
#     ]
# Sample Output:
# [
#     [0, 0, 0], 
#     [0, 0, 20]
# ]

def multiply(m1, m2):
    if len(m1[0]) != len(m2):
        return [[]]
    d1 = dict()
    d2 = dict()
    
    # add non zero positions to d1
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if m1[i][j] != 0:
                d1[(i,j)] = m1[i][j]
    # add non zero positions to d2, with transpose
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            if m2[i][j] != 0:
                d2[(j,i)] = m2[i][j]
    # output matrix of (row-of-m1 x col-of-m2) size
    m3 = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]

    # if col(d1) and col(d2) are equal m3[row(d1)][row(d2)] += value(d1)*value(d2)
    for i,j in d1.keys():
        for x,y in d2.keys():
            if j == y:
                m3[i][x] += d1[(i,j)]*d2[x,y]
    
    return m3

m1 = [
    [0, 2, 0],
    [0, -3, 5],
    ]
m2 = [
    [0, 10, 0],
    [0, 0, 0],
    [0, 0, 4],
    ]
print(multiply(m1, m2))