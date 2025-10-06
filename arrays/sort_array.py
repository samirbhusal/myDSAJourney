# Check if an Array is Sorted
# arr[] = [10, 20, 30, 5, 6]
def isSorted(arr):
    n = len(arr)
    for i in range(1, n):
        if (arr[i-1] > arr[i]):
            return False
    return True


# calling

arr = [10, 20, 30, 40, 50]
print(isSorted(arr))
print(isSorted([10,20,30,60,50]))
