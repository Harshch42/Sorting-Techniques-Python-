# Bubble sort ( Take 2 elements and swap them accordingly and iteratively starting from 1st 2 elements , Typically we iterate n-1 times)
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
