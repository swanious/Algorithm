function solution(scores) {
  var answer = "";
  const len = scores.length;
  const newArr = zip(scores);
  const result = "";
  newArr.map((row, y) => {
    const maxVal = Math.max(...row);
    const minVal = Math.min(...row);
    const newRow = [...row];

    if (checkOnly(newRow, maxVal, minVal, row[y])) newRow.splice(y, 1);
    answer += getRank(
      newRow.reduce((acc, cur) => acc + cur, 0),
      newRow.length
    );
  });
  return answer;
}

// same with zip() of Python
const zip = (arr) => {
  const len = arr.length;
  const newArr = Array.from(Array(len), () => Array().fill([]));
  arr.map((row, y) => {
    row.map((col, x) => {
      newArr[x].push(col);
    });
  });
  return newArr;
};

/**
 * @returns {String}
 * */
const getRank = (sumOfScore, l) => {
  const averageOfScore = Math.floor(sumOfScore / l);

  if (averageOfScore >= 90) return "A";
  else if (averageOfScore >= 80) return "B";
  else if (averageOfScore >= 70) return "C";
  else if (averageOfScore >= 50) return "D";
  else return "F";
};

// 유일하면 true 아니면 false
const checkOnly = (arr, maxVal, minVal, val) => {
  let cnt = 0;
  const valIdx = arr.indexOf(val);
  const restArr = arr.filter((_, i) => i !== valIdx);
  restArr.map((v) => (v === val ? cnt++ : null));
  if (maxVal === val || minVal === val) {
    return cnt > 0 ? false : true;
  }
};
