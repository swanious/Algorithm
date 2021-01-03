### 문제

> 괄호로 된 입력값이 올바른지 판별하라.

- 입력

```python
(){}[]
```

- 출력

```python
True
```

### 풀이

- 딕셔너리에 존재 유무를 if문으로 판별할 때, keys값으로 판별하게 된다.
  - '(, {, [' 는 딕셔너리 brackets의 keys에 없으므로 if 문으로 들어간다.
  - '), }, ]' 는 딕셔너리 brackets의 keys에 있으므로 elif문으로 들어간다.

```python
class Solution(object):
    def isValid(self, s):
        stack = []
        brackets =  {
            ']':'[',
            '}':'{',
            ')':'('
        }
        
        for char in s:
            if char not in brackets:
                stack.append(char)
            elif not stack or brackets[char] != stack.pop():
                return False
        return len(stack) == 0
```





