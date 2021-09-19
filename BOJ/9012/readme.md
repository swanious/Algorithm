# 9012 괄호

> [문제 링크](https://www.acmicpc.net/problem/9012)

## 설계

- check 함수
  - stack이 비었고, 문자가 `)`면 false
  - stack에 값이 있고, 문자가 `)`면 `pop()`
  - 아니면 stack에 push
- 최종 stack의 길이에 따라 결과 출력

## 나의 코드

```javascript
const fs = require("fs");

const stdin = fs.readFileSync("/dev/stdin").toString().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const check = (str) => {
  let stack = [];
  for (let s of str) {
    if (stack.length == 0 && s == ")") return false;

    if (stack.length > 0 && s == ")") {
      stack.pop();
    } else {
      stack.push(s);
    }
  }
  return stack.length === 0;
};

const n = Number(input().trim());
for (let i = 0; i < n; i++) {
  const str = input().trim();
  check(str) ? console.log("YES") : console.log("NO");
}
```

## 후기

- 스택 기초 문제 !
