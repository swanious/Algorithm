def longestPalindrome(s):
    length, sub = 0, ""
    for l in range(len(s)):
        for r in range(l+1, len(s)+1):
            tmp = s[l:r]
            if tmp == tmp[::-1] and len(tmp) > length:
                sub = ''.join(tmp)
                length = len(tmp)
            else:
                continue

    return sub

s = "babad"
print(longestPalindrome(s))
