def merge(lst , l ,mid ,r):
    n1 , n2 = mid - l + 1 , r - mid
    a = [lst[l + i] for i in range(n1)]
    b = [lst[mid + 1 + i] for i in range(n2)]
    i , j , k = 0 , 0 , l
    while i < n1 and j < n2:
        if a[i] < b[j]:
            lst[k] = a[i]
            k += 1
            i += 1
        else:
            lst[k] = b[j]
            j += 1
            k += 1
    while i < n1:
        lst[k] = a[i]
        k += 1
        i += 1

    while j < n2:
        lst[k] = b[j]
        j += 1
        k += 1        

def mergeSort(lst , l , r):
    if l < r:
        mid = (l + r)//2
        mergeSort(lst , l , mid)
        mergeSort(lst , mid + 1 , r)
        merge(lst , l , mid , r)

lst = [12,3,4,1,2,31,0,-1]
mergeSort(lst,0,len(lst) - 1)
print(lst)
