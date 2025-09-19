#1 Find Palindrome - reads the same forward as backward

def check_Palindrome(text):
    left = 0
    right = len(text)-1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True

#2 Pair of numbers (int) that sum to target
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

print(check_for_target([1, 2, 3, 4, 5], 9))
print(check_for_target([1, 2, 3, 4, 5], 6))
