# Rotate Matrix By 90 Degree in Clockwise Direction

# 1 2 3 4                    13 9 5 1
# 5 6 7 8                    14 10 6 2
# 9 10 11 12                 15 11 7 3
# 13 14 15 16                16 12 8 4

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix = [[1,2],[3,4]]
tMatrix = []

for i in range(len(matrix)):
    temp = []
    for j in range(len(matrix[0])):
        temp.append(matrix[j][i])
    tMatrix.append(temp[::-1])

for row in tMatrix:
    print(*row)