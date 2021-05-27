### 문제

> 반복되는 문자를 제외한 가장 긴 문자열의 길이를 출력하라.
>
> - `0 <= s.length <= 5 * 10^4`
> - `s` 는 영문자, 숫자, 공백을 포함한다.

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### 풀이

`s`의 길이가 50000이므로 O(n)안에 풀어야한다.

문제는 슬라이딩 윈도우를 활용하여 풀었다.

1. for문을 돌면서
2. 중복 문자가 존재하지 않는다면 add를 하고, 답은 기존의 `res`와 `인덱스의 차이` 중 큰 값을 넣는다.
3. 중복 문자가 존재하면, 중복문자가 존재할동안 슬라이딩 윈도우를 옮기면서 중복 문자를 제거하고, left의 크기를 +1해준다.

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        res, left = 0, 0
        
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
                
            charSet.add(s[right])
            res = max(res, right - left + 1)
        
        return res

```

