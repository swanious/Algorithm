### 문제

> 인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.

- 입력

```python
m = 2, n = 4
1 -> 2 -> 3 -> 4 -> 5 -> NULL
```

- 출력

```python
1 -> 4 -> 3 -> 2 -> 5 -> NULL
```

### 풀이

- m에서 n의 구간까지 연결리스트를 반복 구조로 노드를 바꿔가면서 이어주는 방식으로 풀이했다.

- 바꿀 필요없는 (m-1)까지의 숫자를 미리 start에 저장해놓는다. (추후 이어주기 위해)

- 바꾸는 구간의 처음을 end로 초기화하고, (n-m)의 횟수로 for문을 돌면서 start, tmp, end 세 개의 변수로 다중 할당을 통해 답을 구한다.

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        # 예외 처리
        if head is None:
            return None
        # return을 root.next로 하기 위함
        root = start = ListNode(None)
        root.next = head
        
        # start와 end의 초기화
        for _ in range(m - 1):
            start = start.next
        end = start.next
        
        # 연결리스트 구해주기
        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
            
        return root.next
```

