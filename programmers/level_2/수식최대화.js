function solution(expression) {
  const regexOfNumber = /[^\+|\*|\-][0-9]{0,3}/g; // 숫자만 뽑기위한 정규표현식
  const regexOfOp = /\+|\-|\*/g; // 연산자만 뽑기위한 정규표현식(우선순위 분류를 위해)

  const arr = expression.match(regexOfNumber); // 숫자배열
  const opArr = expression.match(regexOfOp); // 연산자배열

  // 우선순위를 위한 변수(연산자 중복제거 배열, 배열 길이, 방문체크)
  const opSet = [...new Set(expression.match(regexOfOp))];
  const n = opSet.length;
  const visit = new Array(opSet.length).fill(false);

  // 우선순위 별로 뽑힌 연산자 배열
  const prior = getPrior(n, opSet, [], visit, []);
  let maxNumber = 0;
  let answer = [];

  prior.forEach((v) => {
    let stack = [...arr];
    let opStack = [...opArr];
    for (const op of v) {
      // v는 우선순위에 따른 연산자 배열을 반복문으로 돌면서 연산 -> (배열이 우선순위에 따른 순서로 되어있기 때문에 순서대로 돌면 됨)
      if (op === "-") {
        // '-'연산자가 없어질때까지 계속 연산
        while (opStack.includes("-")) {
          for (let i = 0; i < stack.length; i++) {
            if (opStack[i] === op) {
              // 숫자 배열에서 연산자에 따른 연산 후 다시 삽입(i번째부터 2개를 뽑고, i번째에 연산한 값 삽입)
              stack.splice(i, 2, parseInt(stack[i]) - parseInt(stack[i + 1]));
              // 연산 후 연산자 배열에서 해당 연산자를 제거
              opStack.splice(i, 1);
              // 연산자가 같다면 맨 왼쪽이 우선순위가 크므로, 순차적으로 연산해야함! 그래서 한번 연산 후 break!
              break;
            }
          }
        }
      } else if (op === "+") {
        while (opStack.includes("+")) {
          for (let i = 0; i < stack.length; i++) {
            if (opStack[i] === op) {
              stack.splice(i, 2, parseInt(stack[i]) + parseInt(stack[i + 1]));
              opStack.splice(i, 1);
              break;
            }
          }
        }
      } else if (op === "*") {
        while (opStack.includes("*")) {
          for (let i = 0; i < stack.length; i++) {
            if (opStack[i] === op) {
              stack.splice(i, 2, parseInt(stack[i]) * parseInt(stack[i + 1]));
              opStack.splice(i, 1);
              break;
            }
          }
        }
      }
    }
    // 모든 연산이 끝나면 stack에 마지막 연산값이 들어가있다.
    answer.push(...stack);
  });
  maxNumber = Math.max(...answer.map((v) => Math.abs(v)));
  return maxNumber;
}

const getPrior = (n, arr, newArr, visit, results) => {
  if (newArr.length === n) {
    results.push([...newArr]);
  }

  for (let i = 0; i < n; i++) {
    if (newArr.includes(arr[i])) continue;
    visit[i] = true;
    newArr.push(arr[i]);
    getPrior(n, arr, newArr, visit, results);
    newArr.pop();
    visit[i] = false;
  }
  return results;
};
