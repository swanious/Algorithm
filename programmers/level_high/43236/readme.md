# 43236 징검다리

> [문제 링크](https://programmers.co.kr/learn/courses/30/lessons/43236)

## 문제를 들어가기 전에

- 파트가 이분탐색에 들어있었지만 처음에는 이분탐색 문제라고 판단하기 어려웠지만 이분탐색 문제라고하니 어떤 기준으로 이분탐색을 진행해야하는지 파악해야했다.
- 다른 분들을 참고해보니 바위 사이의 거리를 기준으로 거리를 누적하면서 mid가 누적값보다 작으면 제거하는 방식으로 진행한분도 있었고, 바위를 기준으로 while문 안에서 각각 거리를 구해보면서 하는 방식이 있었다. 하지만, 바위를 기준으로 하면 현재의 위치에 따라 start, end 값만 바꿔주면 됐기에 코드가 편해보였다.

## 설계

1. 이분탐색이므로 rocks를 기준으로 정렬 때린다.
2. start, end는 바위의 시작위치, 끝위치(distance)로 정했다.
3. while문 안에서 중요한건 `mid`, `제거한 바위 수`, `현재 위치`다.
   - `mid`는 바위를 제거하거나, 살리거나를 판단하는 기준이자, 제거된 바위의 수에 따라(n보다 작거나 같으면) 답이될 수 있는 변수이다.
   - `제거한 바위 수`는 바위 위치를 순회하면서 바위와 `현재 위치`의 차이가 `mid`보다 작으면 바위를 제거한다.
   - 그렇지 않으면 `현재의 위치`를 바위의 위치로 변경한다.(이후 바위 사이의 거리를 구하기 위해)
   - 반복문이 끝나고 `제거한 바위 수`가 `n`보다 크다면 더 적게 제거해야하므로 end값을 mid - 1로 변경한다.
   - 그렇지 않으면 더 제거할 수 있으므로 답에 mid를 저장해두고, start값을 mid + 1로 변경한다.
4. while이 끝나면 answer에는 제거할 수 있는 바위의 수에따른 최적의 mid값이 저장되어있다.

## 나의 코드

```javascript
function solution(distance, rocks, n) {
  let start = 0;
  let end = distance;
  let answer = 0;

  rocks.sort((a, b) => a - b);

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    let removeCnt = 0;
    let currentPos = 0;

    for (let i = 0; i < rocks.length; i++) {
      if (rocks[i] - currentPos < mid) {
        removeCnt++;
      } else currentPos = rocks[i];
    }

    if (removeCnt > n) {
      end = mid - 1;
    } else {
      start = mid + 1;
      answer = mid;
    }
  }
  return answer;
}
```

## 후기

- 문제를 딱 보고 이분탐색이라고 생각하진 못했다.
- [링크](https://deok2kim.tistory.com/122)를 참고했다. 자세한 풀이가 나와있어서 좋은 참고가됐다.
