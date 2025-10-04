#1 Pair of numbers (int) that sum to target
def check_for_target(nums, target):
    left = 0
    right = len(nums)-1
    while left < right:
        current_Sum = nums[left] + nums[right]
        if current_Sum == target:
            return True

        if current_Sum > target:
            right -= 1
        else:
            left += 1
    return False

#Leaders in an array
# Given an array arr[] of size n, the task is to find all the Leaders in the array.
# An element is a Leader if it is greater than or equal to all the elements to its right side.

def checkLeaderInArray(nums):
    leaders = []
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            if nums[i] < nums[j]:
                break
        else:
            leaders.append(nums[i])

    return leaders

# Using Suffix Maximum - O(n) Time and O(1) Space:
def  checkLeaderInArr_SuffixMax(nums):
    resultArr = []
    n = len(nums)

    maxRightEle = nums[-1]
    resultArr.append(maxRightEle)

    for i in range(n-2, -1, -1):
        if nums[i]  > maxRightEle:
            maxRightEle = nums[i]
            resultArr.append(maxRightEle)

    resultArr.reverse()
    return resultArr

