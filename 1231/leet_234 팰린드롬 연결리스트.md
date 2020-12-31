### 문제

![image-20201231171049748](leet_234%20%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC%20%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8.assets/image-20201231171049748.png)

### 풀이

내장 자료구조인 deque를 사용하는 것은 기본적이므로 생략하고, `런너`기법을 이용해 풀이를 해보고 학습했다.

- 런너 기법
  - 런너는 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법이다.
  - 빠른 런너(2칸씩) 느린 런너(1칸씩)라고 부르는 2개의 포인터를 이용하여, 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있다.
  - 문제 풀이에서는 빠른 런너가 연결 리스트의 끝에 도달하면, 느린 런너는 정확히 연결 리스트의 **중간 지점**을 가리키게 된다. 여기서부터 값을 비교하거나 뒤집기를 시도하면서 팰린드롬을 찾게 된다.

- 코드

```python
class Solution(object):
    def isPalindrome(self, head):
        rev = None # 느린 런너가 중간지점일 때 비교할 대상(뒤집어진 상태)
        slow = fast = head
        
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            # 다중할당에 대해서는 자세한 이해가 필요하다
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
            
        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
```

### 다중 할당

```python
# 이 코드를 보면서, 처음에 무슨 내용인지 이해하는데 오랜 시간이 걸렸다.
rev, rev.next, slow = slow, rev, slow.next

# 위의 코드를 아래처럼 바꾸면 어떨까?
rev, rev.next = slow, rev
slow = slow.next

# 실행시켜보면 위와 동일한 값이 나오지 않는다. 왜 그럴까?
```

위의 `rev, rev.next = slow, rev`와 `slow = slow.next`를 나눠서 하면 slow와 rev가 동일한 참조를 하게 된다.

예로, **rev = 1, slow = 2 ->3**라고 가정해보면, slow는 연결리스트이고, **slow.next**는 3이라는 의미이다. 하지만, 첫줄을 실행하면, **rev = 2 -> 3, rev.next = 1**이 되고, **rev = 2->1**이 된다. 즉, 동일한 참조를 하고 있는 **slow 또한 3이 아닌 1로 바뀐다는 의미**이다.



그럼 위의 3개를 다중 할당한 코드는 어떨까?

rev = 2 -> 3, rev.next = 1, slow = 3이다. 여기서 rev = 2 -> 1로 바뀌지만, 여전히 slow는 3을 가리킨다. 즉, 이러한 특성에 대해 깊은 이해가 필요할 것 같다.

결과적으로, 맨 위처럼 3개를 다중할당하지 않으면 문제는 풀리지 않는다.