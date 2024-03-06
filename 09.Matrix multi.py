lst1=[[1,2,3],[4,5,6],[7,8,9]]
lst2=[[10,11,12],[13,14,15],[16,17,18]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(lst1)):
    for j in range(len(lst1[i])):
        for k in range(len(lst1)):
            c[i][k]+=lst1[i][k]*lst2[k][j]
for ans in c:
    print(ans)
