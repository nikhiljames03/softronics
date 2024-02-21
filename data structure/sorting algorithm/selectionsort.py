def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
        return arr
x = int(input("enter a number: "))
y = []
for i in range(x):
    z=int(input("enter a number: "))
    y.append(z)
print(selection_sort(y))