n=int(input())
m=int(input())
matrix=list()
for i in range(n):
    matrix.append(['.']*m)
    for j in range(m):
        if i%2==0 or i==0:
            if j%2==0 or j==0:
                matrix[i][j]='.'
            else:
                matrix[i][j] = ('*')
        else:
            if j%2==0 or j==0:
                matrix[i][j]='*'
            else:
                matrix[i][j] = ('.')
        print(matrix[i][j],end='')
    print()