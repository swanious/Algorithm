/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function (n) {
  const solutions = getNQueensResult(n, 0, [], []);
  return solutions;
};

function getNQueensResult(n, row, choices, solutions) {
  // 재귀 탈출조건
  if (row === n) {
    const processedChoices = processChoices(choices);
    solutions.push(processedChoices);

    return solutions;
  } else {
    for (let i = 0; i < n; i++) {
      // 인덱스를 넣어보고, 검증o -> 재귀, 검증x -> 돌아가기
      choices.push(i);
      if (isValid(choices)) {
        solutions = getNQueensResult(n, row + 1, choices, solutions);
      }
      choices.pop();
    }
  }
  return solutions;
}

// 인덱스 -> 문자
function processChoices(choices) {
  const board = new Array(choices.length).fill("");

  for (let i = 0; i < choices.length; i++) {
    for (let j = 0; j < choices.length; j++) {
      if (choices[i] === j) board[i] += "Q";
      else board[i] += ".";
    }
  }
  return board;
}

// 체스말이 놓여질 수 있는지 검증하는 부분
function isValid(choices) {
  const row = choices.length - 1;
  const column = choices[row];

  for (let i = 0; i < row; i++) {
    const currentRow = i;
    const currentColumn = choices[i];
    const leftCollisionIndex = currentColumn - (row - currentRow); // 왼쪽 대각선
    const rightCollisionIndex = currentColumn + (row - currentRow); // 오른쪽 대각선

    // 같은 열에 위치하면 false
    if (column === currentColumn) return false;

    // 대각선 상에 위치하면 false
    if ((column === leftCollisionIndex) | (column === rightCollisionIndex))
      return false;
  }
  return true;
}
