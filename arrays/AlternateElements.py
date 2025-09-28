#Given an array arr[], the task is to print every alternate element of the array starting from the first element.

#Iterative Approach

def getAlternateEle_Iterative(arr):
    res = []

    # Iterate over all alternate elements
    for i in range(0, len(arr), 2):
        res.append(arr[i])
    return res


arr = [10, 20, 30, 40, 50]
alt = getAlternateEle_Iterative(arr)
print(alt)
print(" ".join(map(str, alt)))

# Recursive Approach

def getAlternateEle_Recursive(arr):
    alteredArr = []



