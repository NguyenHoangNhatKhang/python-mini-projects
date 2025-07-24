def bubble_sort(arr,n):
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]= arr[j+1], arr[j]


arr = [5,6,9,8,3,7]
n = len(arr)
bubble_sort(arr,n)
for i in range(n):
    print(arr[i],end=" ")