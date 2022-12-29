#Selection Sort ( Take the minimum element of the array and swap it with the 1st element and move to the next element untill sorted )
lst = [ 5,3,8,6,7,2 ]
temp = 0
n = len(lst)
for i in range(n-1):
    min_pos = i
    for j in range(i,n):
        if lst[j] < lst[min_pos]:
            min_pos = j
    
    temp = lst[i]
    lst[i] = lst[min_pos]
    lst[min_pos] = temp
print(lst)
