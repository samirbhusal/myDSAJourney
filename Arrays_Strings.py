# Find Palindrome - reads the same forward as backward

def check_Palindrome(text):
    left = 0
    right = len(text)-1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True

print(check_Palindrome("aba"))
print(check_Palindrome("test"))
print(check_Palindrome(""))