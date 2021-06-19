def check(a, i, j, k):
    for x in range(9):
        if a[i][x] == k:
            return False
        if a[x][j] == k:
            return False
    for x in range(i-i%3,i-i%3+3):
        for y in range(j-j%3, j-j%3+3):
            if a[x][y] == k:
                return False
    return True
    
def backtracking(a,i,j):
    if j == 9 and i == 8:
        return True
    if j == 9:
        i = i + 1
        j = 0
    if a[i][j] > 0:
        return backtracking(a,i,j+1)
    for k in range(1,10):
        if check(a,i,j,k) == True:
            a[i][j] = k
            if backtracking(a,i,j+1):
                return True    
        a[i][j] = 0
    
    return False
def printa(a):
    for i in range(0,9):
        for j in range(0,9):
            print(a[i][j]," ", end = '')
        print("")

        
a = [[ 3, 0, 6, 5, 0, 8, 4, 0, 0 ],
    [ 5, 2, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 8, 7, 0, 0, 0, 0, 3, 1 ],
    [ 0, 0, 3, 0, 1, 0, 0, 8, 0 ],
    [ 9, 0, 0, 8, 6, 3, 0, 0, 5 ],
    [ 0, 5, 0, 0, 9, 0, 6, 0, 0 ],
    [ 1, 3, 0, 0, 0, 0, 2, 5, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 7, 4 ],
    [ 0, 0, 5, 2, 0, 6, 3, 0, 0 ]]
if backtracking(a,0,0) == -1:
    print(-1)
else:
    printa(a)
