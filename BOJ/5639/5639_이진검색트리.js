const input = [];
const stack = [];
const result = [];

require('readline')
  .createInterface(process.stdin, process.stdout)
  .on('line', function(line) {
    input.push(Number(line.trim()));
  })
  .on('close', function() {
    // 전위 순회 결과 배열의 시작, 끝 인덱스
    stack.push([0, input.length - 1]);
    while (stack.length) {
      const [start, end] = stack.pop();
      if (start > end) continue;

      let division;

      // 루트보다 큰 숫자 중 처음 만나는 숫자가 오른쪽 서브트리의 루트
      for (let i = start + 1; i <= end; i++) {
        if (input[i] < input[start]) continue;
        division = i;
        break;
      }

      if (division) {
        // 왼쪽 서브트리의 시작, 끝 인덱스
        stack.push([start + 1, division - 1]);
        // 오른쪽 서브트리의 시작, 끝 인덱스
        stack.push([division, end]);
      } else {
        // 루트를 제외한 숫자
        stack.push([start + 1, end]);
      }
      // result 배열의 처음에 루트 삽입
      // while문에서 이 과정 반복하면 후위 순회
      result.unshift(input[start]);
    }
    console.log(result.join('\n'))
  })