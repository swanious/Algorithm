function solution(absolutes, signs) {
  return signs.reduce((acc, cur, i) => cur ? acc + absolutes[i] : acc - absolutes[i], 0);
}