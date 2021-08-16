function solution(places) {
  var answer = [];
  // 방문 체크 배열
  const visit = Array.from(Array(5), () => Array(5).fill(true));

  places.forEach((eachMap) => {
    bfs(eachMap) ? answer.push(1) : answer.push(0);
  });
  return answer;
}

const bfs = (arr) => {
  const dr = [1, 0, 0];
  const dc = [0, -1, 1];
  const posP = getP(arr);
  let check = false;

  posP.forEach(([r, c]) => {
    const q = [[r, c]];
    const v = Array.from(Array(5), () => Array(5).fill(false));

    while (q.length !== 0) {
      let [row, col] = q.shift();
      v[row][col] = true;
      for (let i = 0; i < 3; i++) {
        const nr = row + dr[i];
        const nc = col + dc[i];
        if (nr < 0 || nc < 0 || nr > 4 || nc > 4 || v[nr][nc]) continue;
        if (arr[nr][nc] === "X") continue;
        else if (
          arr[nr][nc] === "O" &&
          Math.abs(nr - r) + Math.abs(nc - c) <= 1
        )
          q.push([nr, nc]);
        else if (
          arr[nr][nc] === "P" &&
          Math.abs(nr - r) + Math.abs(nc - c) <= 2
        ) {
          check = true;
        }
      }
    }
  });
  return check ? false : true;
};

const getP = (arr) => {
  let temp = [];
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (arr[i][j] === "P") temp.push([i, j]);
    }
  }

  return temp;
};
