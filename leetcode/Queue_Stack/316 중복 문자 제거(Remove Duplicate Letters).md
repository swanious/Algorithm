## 문제

> 중복된 문자를 제외하고 사전식 순서로 나열하라.

- 입력

```python
"bcabc"
"cbacdcbc"
```

- 출력

```python
"abc"
"acdb"
```

## 풀이

> '파이썬 알고리즘 인터뷰'책에서 두 가지 풀이로 푼다. 재귀, 스택
>
> 두번째 예시로 사전식 순서로 나열해보면서 이해해보자. 
>
> "cbacdcbc"에서 중복 문자는 c, b가 존재한다. a, d는 중복문자가 존재하지 않으므로 현재의 위치에 자리해야하며, 중복을 제거할 수 있는 c, b는 제거한 후 사전식으로 나열한다.
>
> 예로, ebcabc라면 중복이 없는 e와 a는 그대로 두고, 중복인 b, c를 정리하여 eabc로 나열한다.  

1. 재귀

- 코드도 어렵고 풀이도 어려워서, 그냥 코드를 보고 pycharm의 디버그를 돌려보면서 이해하는데 시간을 썼다. 

```python
class Solution(object):
    def removeDuplicateLetters(self, s):
        # 집합으로 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            
            # 전체 집합과 접미사 집합이 일치할 때 분리 진행
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''
```

```python
s ="cbacdcbc"
sorted(set(s)) = "abcd"
1. suffix = "acdcbc"
   set(suffix)는 abcd
   set(s)는 abcd
   즉, set(suffix) == set(s)이므로 a를 쌓고, a를 제외한 removeDuplicateLetters("cdcbc")로 재귀에 들어간다.

s = "cdcbc"
sorted(set(s)) = "bcd" # for문을 bcd순서로 돔
2. b는 set(s) != set(suffix)임 c로 이동
   c는 set(s) == set(suffix)이므로 c를 쌓고, c를 제외한 removeDuplicateLetters("db")로 재귀에 들어간다.

s = "db"
sorted(set(s)) = "db" # for문을 bcd순서로 돔
3. b는 set(s) != set(suffix)임 c로 이동
   c는 set(s) != set(suffix)임 d로 이동
   d일 때 set(s) == set(suffix)이므로 d를 쌓고,  d를 제외한 removeDuplicateLetters("b")로 재귀에 들어간다.

s = "b"
sorted(set(s)) = "b" # for문을 bc순서로 돔
4. b일 때 set(s) == set(suffix)이므로 b를 쌓고, 재귀가 풀리면서 acdb를 출력한다.
```

