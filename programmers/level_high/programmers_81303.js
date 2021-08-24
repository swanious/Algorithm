// 표 편집 - https://programmers.co.kr/learn/courses/30/lessons/81303?language=javascript
function solution(n, k, cmd) {
  let answer = "";
  const stack = [];
  const nodes = { 0: [n - 1, 1] };
  for (let i = 1; i < n; i++) {
    nodes[i] = i === n - 1 ? [i - 1, 0] : [i - 1, i + 1];
  }

  cmd.forEach((c) => {
    // C Z
    if (c.length > 1) {
      const [command, size] = c.split(" ");
      let cnt = 0;
      k =
        command === "U"
          ? changeCurPos(k, parseInt(size), nodes, "U")
          : changeCurPos(k, parseInt(size), nodes, "D");
    }
    // U D
    else {
      if (c === "C") {
        nodes[nodes[k][0]][1] = nodes[k][1]; // 1, 2, 3중 2가 빠지면 2의 prev인 1의 next를 2의 next인 3로 변경
        nodes[nodes[k][1]][0] = nodes[k][0];
        stack.push([k, nodes[k]]); // 제거하기 전 stack에 저장
        const temp = nodes[k];

        delete nodes[k];

        k = temp[1] === 0 ? temp[0] : temp[1]; // 맨 마지막 idx면 k는 이전의 값
      } else {
        const [idx, val] = stack.pop();
        const [prev, next] = val;
        nodes[idx] = [prev, next]; // 노드 삽입
        // 리스트 연결
        nodes[prev][1] = idx;
        nodes[next][0] = idx;
      }
    }
  });
  for (let i = 0; i < n; i++) {
    nodes[i] === undefined ? (answer += "X") : (answer += "O");
  }
  return answer;
}

const changeCurPos = (k, size, nodes, status) => {
  for (let i = 0; i < size; i++) {
    k = status === "U" ? nodes[k][0] : nodes[k][1];
  }
  return k;
};
