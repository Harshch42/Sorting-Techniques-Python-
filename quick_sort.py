def quick_Sort(lst):
    lst_smaller = []
    lst_greater = []
    n = len(lst)
    
    if  n <= 1:
        return lst
    else:
        pivot = lst.pop()
        
    for i in lst:
        if i <= pivot:
            lst_smaller.append(i)
        else:
            lst_greater.append(i)
    return quick_Sort(lst_smaller) + [pivot] + quick_Sort(lst_greater)

lst = [21,38,16,7,36,17]

print(quick_Sort(lst))
