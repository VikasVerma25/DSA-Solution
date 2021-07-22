def insertion(a, n):
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min = j
        a[i],a[min] = a[min],a[i]

a = [4,6,9,2,1,5,7,4]
insertion(a,len(a))
print(a)
