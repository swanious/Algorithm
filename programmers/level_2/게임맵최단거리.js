function solution(maps) {
  var answer = 0;

  // n, m
  const n = maps.length;
  const m = maps[0].length;

  // 방향
  const dy = [1, 0, -1, 0];
  const dx = [0, 1, 0, -1];

  // queue와 visit 배열 초기화
  let q = [];
  const visit = Array.from(Array(n), () => Array(m).fill(false));
  visit[0][0] = true;

  // y, x, 거리
  q.push([0, 0, 1]);

  // bfs 시작
  while (q.length > 0) {
    let [y, x, d] = q.shift();
    if (y === n - 1 && x === m - 1) {
      answer = d;
      break;
    }
    // 4방향 체크
    for (let i = 0; i < 4; i++) {
      // 미리 가볼 분신들
      let ny = y + dy[i];
      let nx = x + dx[i];
      // 분신이 벽 / 장애물 / 방문체크하고 갈 수 있으면,
      if (
        ny >= 0 &&
        ny < n &&
        nx >= 0 &&
        nx < m &&
        maps[ny][nx] === 1 &&
        !visit[ny][nx]
      ) {
        // 갈 곳 방문체크, q에 넣어주기
        visit[ny][nx] = true;
        q.push([ny, nx, d + 1]);
      }
    }
  }

  // n-1, m-1위치(상대방 진영)에 방문하지 않았으면 -1 반환하고, 아니면 answer반환
  return !visit[n - 1][m - 1] ? -1 : answer;
}
