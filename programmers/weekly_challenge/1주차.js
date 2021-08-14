function solution(price, money, count) {
  let sum = 0;
  let cnt = 1;
  for (let i = 0; i < count; i++) {
    sum += price * cnt;
    cnt++;
  }
  return sum - money > 0 ? sum - money : 0;
}
