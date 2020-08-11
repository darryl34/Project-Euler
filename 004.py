# Problem 4 - Largest Palindrome Product

def palindrome():
    ans = (i*j for i in reversed(range(100, 1000)) for j in reversed(range(100, 1000)) if str(i*j) == str(i*j)[::-1])
    return max(ans)

print(palindrome())