def Insertion_Sort(lst):
    for i in range(1,len(lst)):
        temp = lst[i]
        j = i-1
        while j>=0 and temp < lst[j]:
            lst[j+1] = lst[j]
            j = j-1
        lst[j+1] = temp
    print(lst)


lst = [21,38,16,7,36,17]
Insertion_Sort(lst)
