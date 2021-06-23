function solution(s) {
  // 문자열의 갯수가 홀수면 0
  if (s.length % 2 != 0) return 0;

  var sArr = [...s];
  var stack = [];

  for (var i = 0; i < sArr.length; i++) {
    if (stack && stack[stack.length - 1] === sArr[i]) {
      stack.pop();
      continue;
    }
    stack.push(sArr[i]);

    // 남은 문자열의 갯수가 stack의 길이보다 작으면 0
    if (sArr.length - i < stack.length) return 0;
  }

  return 1;
}
