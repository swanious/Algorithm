function solution(w, h) {
  var maxV = Math.max(w, h);
  var minV = Math.min(w, h);

  if (w === h) return w * h - w;
  if (w === 1 || h === 1) return 0;

  // 흰색은 너비 + 높이 - 최대공약수
  var white = w + h - gcd(maxV, minV);

  var gray = w * h - white;
  return gray;
}

/*
  유클리드 호재법으로 최대 공약수 구하기
  a를 b로 나눈 나머지를 r이라고 할 때, b와 r의 최대공약수가 a와 b의 최대공약수이다.
  a % b = r ->  b % r = r' -> ... 
  이렇게 재귀 형식으로 나누다가 나머지가 0이 되면, 그때의 값이 최대공약수이다.
*/
var gcd = (n1, n2) => {
  return n1 % n2 === 0 ? n2 : gcd(n2, n1 % n2);
};
