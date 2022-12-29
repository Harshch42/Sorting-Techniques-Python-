def Binary_Search(lst , val):
    lst.sort()
    l = 0
    u = len(lst)-1
    while l<=u:
        mid = (l+u) // 2
        
        if lst[mid] == val:
            return ("Value is at "+"Position "+f"{mid}")
        elif lst[mid] < val:
            l = mid
        elif lst[mid] > val:
            u = mid
        else:
            return ("Element not in list")


lst = [ 5,3,8,6,7,2 ]
val = 7
res = Binary_Search(lst,val)
print(res)
