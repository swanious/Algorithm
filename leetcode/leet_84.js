/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function (heights) {
  var index = 1;
  var result = 0;
  var stack = [[0, 0]];

  // 마지막 계산을 위해서 추가
  heights.push(0);

  for (var height of heights) {
    var flag = 0; // 높이가 줄었을 경우의 높이가 유지된 상태의 가장 이전의 index

    // stack의 peek가 현재 높이보다 크면,
    while (stack[stack.length - 1][0] > height) {
      // 마지막 [높이, 인덱스]를 pop한 것을 temp 변수에 저장
      var temp = stack.pop();

      //  이때까지의 넓이를 계산한다.
      var block = (index - temp[1]) * temp[0];

      // 높이가 유지된 상태에서 가장 이전 index 저장
      flag = temp[1];

      // max값 찾기
      result = Math.max(result, block);
    }

    if (stack[stack.length - 1][0] !== height) {
      if (!flag) {
        stack.push([height, index]);
      } else {
        stack.push([height, flag]);
      }
    }
    index += 1;
  }
  return result;
};
