function solution(d, budget) {
  var answer = 0;
  d.sort((a, b) => (a > b ? 1 : -1));
  for (let c of d) {
    if (c > budget) break;
    else {
      budget -= c;
      answer++;
    }
  }
  return answer;
}
