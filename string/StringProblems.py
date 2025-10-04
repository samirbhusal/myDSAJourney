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