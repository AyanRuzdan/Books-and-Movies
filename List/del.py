mat = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
arr = []
for i in range(3):
    row = (list(map(int, input().split())))
    arr.append(row)
for i in range(3):
    for j in range(3):
        if (arr[i][j] and 1):
            mat[i][j] ^= 1
            mat[max(i-1, 0)][j] ^= 1
            mat[min(i+1, 2)][j] ^= 1
            mat[i][max(j-1, 0)] ^= 1
            mat[i][min(j+1, 2)] ^= 1
for i in range(3):
    for j in range(3):
        print(mat[i][j], end="")
    print()