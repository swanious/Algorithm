function solution(n, edge) {
  var matrix = Array.from(Array(n + 1), () => Array());
  var visit = new Array(n + 1).fill(false);
  var minDis = new Array(n + 1).fill(Number.MAX_SAFE_INTEGER);

  // 인접 리스트
  for (var e of edge) {
    matrix[e[0]].push(e[1]);
    matrix[e[1]].push(e[0]);
  }

  var q = [];
  q.push(1);

  minDis[0] = 0;
  minDis[1] = 0;
  visit[1] = true;
  while (q.length) {
    var from = q.shift();
    matrix[from].forEach((to) => {
      // 방문 체크
      if (!visit[to]) {
        visit[to] = true;
        q.push(to);
      }
      // 거리 저장
      minDis[to] =
        minDis[to] > minDis[from] + 1 ? minDis[from] + 1 : minDis[to];
    });
  }
  var max = Math.max(...minDis);
  var answer = minDis.filter((d) => d === max);
  return answer.length;
}
