def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        elif x > pivot:
            right.append(x)
    return quicksort(left) + middle + quicksort(right)


x = int(input("enter a number: "))
y = []
for i in range(x):
    z=int(input("enter a number: "))
    y.append(z)
print(quicksort(y))