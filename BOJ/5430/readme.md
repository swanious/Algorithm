# 5430 AC

> [문제 링크](https://www.acmicpc.net/problem/5430)

## 설계

- 처음 입력받을 때 `\r\n`을 기준으로 split()해주면 입력이 훨씬 편해진다.
- 배열을 뒤집는 `R`커맨드는 실제 배열을 돌려줄필요가 전혀없다.
  - R이 나올때마다 배열에서 지워야하는 위치만 `0 or arr.length-1`로 변화하므로 idx만 그때마다 변경시켜주고 해당 인덱스의 문자열을 지우면된다.
  - R이 몇번나왔는지 카운팅해서 홀수일때는 마지막 배열만 한번 뒤집어주고, 짝수면 그대로 반환한다.
- 마지막에 배열을 JSON.stringify()를 통해 문자열 형변환해줘야한다.

## 나의 코드

```javascript
// 입출력
// const stdin = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const stdin = require("fs").readFileSync("test.txt").toString().split("\r\n");
const input = (() => {
  let l = 0;
  return () => stdin[l++];
})();

const T = +input();
for (let tc = 0; tc < T; tc++) {
  const cmd = input().split("");
  const _ = +input();
  const arr = input()
    .replace(/[\[\]]/g, "")
    .split(",")
    .filter((v) => v)
    .map(Number);

  let idx = 0;
  let rCnt = 0;
  let check = false;

  cmd.forEach((c) => {
    if (c === "R") {
      rCnt++;
      idx = idx === 0 ? arr.length - 1 : 0;
    } else {
      if (arr.length === 0) {
        check = true;
        return;
      }
      arr.splice(idx, 1);
      if (idx > 0) idx -= 1;
    }
  });
  console.log(
    check
      ? "error"
      : rCnt % 2
      ? JSON.stringify(arr.reverse())
      : JSON.stringify(arr)
  );
}
```

## 후기

- 마지막 배열 형변환을 안해줘서 채점현황 한바닥을 `틀렸습니다`로 도배했다.
