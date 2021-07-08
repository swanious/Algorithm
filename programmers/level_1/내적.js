function solution(a, b) {
  var answer = 0;
  for (let i = 0; i < a.length; i++) {
    let sum = a[i] * b[i];
    answer += sum;
  }
  return answer;
}
