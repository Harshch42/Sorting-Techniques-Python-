lst = [ 5,3,8,6,7,2 ]
temp = 0
n = len(lst)
for j in range(n-1,0,-1):
    for i in range(j):
        if lst[i]>lst[i+1]:
            temp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = temp
print(lst)