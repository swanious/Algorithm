# 43164 여행경로

> [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/43164)

## 설계

1. tickets를 오름차순 정렬
2. [시작점, 방문횟수]로 dfs 진행
   - 배열의 첫번째 값(`tickets[i][0]`)이 방문하지 않은 곳이고, 출발지와 같으면,
   - `tickets[i][1]`이 다음 갈 곳이므로 `dfs(tickets[i][1], cnt + 1)` 탐색
   - dfs를 모두 순회해도 여행경로가 없으면 visit를 false로 돌려주고, 배열에서 경로 pop
3. 여행횟수와 tickets의 길이가 같으면 return후 답 출력

## 나의 코드

```python
def solution(tickets):
    l = len(tickets)
    visit = [False] * l
    ans = []

    tickets.sort()

    def dfs(start, cnt):
        global answer
        ans.append(start)

        if cnt == l:
            return True

        for i in range(l):
            if not visit[i] and tickets[i][0] == start:
                visit[i] = True
                if dfs(tickets[i][1], cnt + 1): return True
                visit[i] = False

        ans.pop()
        return False

    dfs('ICN', 0)
    return ans
```

```javascript
function solution(tickets) {
  let answer = [];
  const temp = []; // dfs를 돌면서 값을 저장할 배열
  const visit = [];
  const len = tickets.length;

  tickets.sort();

  const dfs = (start, depth) => {
    temp.push(start); // 재귀 시작과 함께 값을 저장

    if (depth === len) {
      // temp를 그냥 반환해도 되지만, boolean타입으로 반환하면 효율적으로 조건에 따른 로직을 구현할 수 있다.
      answer = temp;
      return true;
    }

    for (let i = 0; i < len; i++) {
      if (!visit[i] && tickets[i][0] === start) {
        // 예제1번의 처음이라고 생각하면 ["ICN", "JFK"]에 조건이 부합되어 if문으로 들어옴
        visit[i] = true;

        if (dfs(tickets[i][1], depth + 1)) return true; // depth와 len이 같을 때 여기로 빠져서 바로 답 출력

        visit[i] = false; // 답을 구하지 못했으므로 다시 false로 돌림
      }
    }
    // 여기까지 왔다는 뜻은 반복문을 다 돌아도 답을 구하지 못했다는 의미
    temp.pop();
    return false;
  };

  dfs("ICN", 0);
  return answer;
}
```

## 후기

- 오름차순 정렬(가능한 경로가 2개 이상이면 알파벳 순서를 지켜야함)
- 갈 수 있는 경로면 들어가보고 아니면 빼면서 답을 구해주면 된다.
