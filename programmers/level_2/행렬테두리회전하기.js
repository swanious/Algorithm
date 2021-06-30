// https://programmers.co.kr/learn/courses/30/lessons/77485#qna

/*
  구현하는 부분 + 깊은 복사에서 살짝 애먹었다 ㅠ 2차원 배열의 경우 열까지 깊은 복사를 해야 같은 위치를 참조하지 않는다.
  각 테두리만 시계방향을 돌아야 하는데, 테두리가 아닌 곳은 y1 < 행 < y2 && x1 < 열 < x2 이므로 continue로 스킵한다.
  테두리 부분은 그냥 구현 문제로 상, 하, 좌, 우를 각각 조건을 나눠 구해주고, 새로운 배열을 저장한다.
  이후, 이전에 저장한 배열을 깊은 복사하여 queries에 따른 위치를 회전시키면 끗!
*/
function solution(rows, columns, queries) {
  var answer = [];
  let arr = makeArr(rows, columns);

  queries.forEach((v) => {
    const temp = makeArr(rows, columns);

    // 깊은 복사하기 (temp = [...arr]를 할 경우 각 행만 얕은복사가 됨)
    for (let row = 0; row < rows; row++) {
      temp[row] = [...arr[row]];
    }
    let minVal = Number.MAX_SAFE_INTEGER;
    let [y1, x1, y2, x2] = [...v];

    // 편한 계산을 위해 -1
    y1 -= 1;
    x1 -= 1;
    y2 -= 1;
    x2 -= 1;

    for (let i = y1; i < y2 + 1; i++) {
      for (let j = x1; j < x2 + 1; j++) {
        // 테두리가 아닌 곳은 바꾸지 않고 continue
        if (i > y1 && j > x1 && i < y2 && j < x2) continue;
        else {
          // 현재 내가 회전하는 곳에서의 가장 작은 값을 뽑기
          minVal = Math.min(minVal, arr[i][j]);

          // 행렬 테두리를 회전합니다.
          // 1. 왼쪽 열
          if (i < y2 && j === x1) {
            temp[i][j] = arr[i + 1][j];
            // 2. 위 행
          } else if (i === y1 && j <= x2) {
            temp[i][j] = arr[i][j - 1];
            // 3. 오른쪽 행
          } else if (i <= y2 && j === x2) {
            temp[i][j] = arr[i - 1][j];
            // 4. 아래 행
          } else if (i === y2 && j <= x2) {
            temp[i][j] = arr[i][j + 1];
          }
        }
      }
    }
    // 작은 값 저장 및 새로운 배열 arr에 덮어씌우기
    answer.push(minVal);
    arr = temp;
  });
  return answer;
}

// 행렬 생성 함수
const makeArr = (rows, columns) => {
  let arr = Array.from(Array(rows), () => Array(columns).fill(0));
  let cnt = 1;
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < columns; j++) {
      arr[i][j] = cnt;
      cnt++;
    }
  }
  return arr;
};
