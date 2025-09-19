#3 find lowest value in array/list
arr = [20,30,14,5,60,7,80,9]
minVal = arr[0]
for i in arr:
    if i < minVal:
        minVal = i
print("Min Value: ",minVal)