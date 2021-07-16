function solution(n, results) {
  var answer = 0;
  var visit = Array.from(Array(n), () => Array(n).fill(0));

  for (var r of results) {
    visit[r[0] - 1][r[1] - 1] = 1;
    visit[r[1] - 1][r[0] - 1] = -1;
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (visit[i][j] === 1) {
        let index = [];
        // A를 이긴 사람들은 A에게 패배한사람한테 무조건 이긴다. (반대도 성립)
        visit[i].map((v, idx) => {
          if (v === -1) index.push(idx);
        });
        index.map((v) => {
          visit[j][v] = -1;
        });
      } else if (visit[i][j] === -1) {
        let index = [];
        visit[i].map((v, idx) => {
          if (v === 1) index.push(idx);
        });
        index.map((v) => {
          visit[j][v] = 1;
        });
      }
    }
  }
  visit.map((v) => {
    if (v.filter((v) => v === 0).length === 1) answer++;
  });
  return answer;
}
