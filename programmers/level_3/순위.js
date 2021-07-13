function solution(n, results) {
  var answer = 0;
  var G = Array.from(Array(n + 1), () => Array());

  for (var r of results) {
    G[r[1]].push(r[0]);
  }

  for (var i = 1; i < n + 1; i++) {
    var q = [];
    var minDis = new Array(n + 1).fill(Number.MAX_SAFE_INTEGER);

    minDis[i] = 0;
    var visited = new Array(n + 1).fill(false);
    q.push(i);

    while (q.length) {
      var from = q.pop();

      G[from].forEach((to) => {
        if (!visited[to]) {
          visited[to] = true;
          q.push(to);
        }
        minDis[to] =
          minDis[to] > minDis[from] + 1 ? minDis[from] + 1 : minDis[to];
      });
    }
    minDis.filter((v, idx) => {
      if (v == Number.MAX_SAFE_INTEGER || idx === 0) return;
    });
  }
  return answer;
}
