def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
x = int(input("enter a number: "))
arr= []
for i in range(x):
    z=int(input("enter a number: "))
    arr.append(z)
insertion_sort(arr)
print(arr)