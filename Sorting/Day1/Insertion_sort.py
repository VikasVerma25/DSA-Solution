def insertion(a,n):
    for i in range(1,n-1):
        pos = a[i]
        j = i-1
        while j>=0 and pos<a[j]:
            a[j+1]=a[j]
            j -= 1
        a[j+1] = pos
        
a = [2,3,1,6,4,8,5]
insertion(a,len(a))
print(a)