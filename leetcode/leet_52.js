/**
 * @param {number} n
 * @return {number}
 */
var totalNQueens = function (n) {
  var solutions = getNQueens(0, n, [], []);
  return solutions.length;
};

const getNQueens = (row, n, choices, solutions) => {
  if (row === n) {
    solutions.push(choices);
    return solutions;
  } else {
    for (let i = 0; i < n; i++) {
      choices.push(i);
      if (isValid(choices)) {
        getNQueens(row + 1, n, choices, solutions);
      }
      choices.pop();
    }
  }
  return solutions;
};

const isValid = (choices) => {
  const row = choices.length - 1;
  const column = choices[row];

  for (let i = 0; i < row; i++) {
    const currentRow = i;
    const currentColumn = choices[i];
    const leftDigonalIdx = currentColumn - (row - currentRow);
    const rightDigonalIdx = currentColumn + (row - currentRow);

    if (column === currentColumn) return false;
    if ((column === leftDigonalIdx) | (column === rightDigonalIdx))
      return false;
  }
  return true;
};
