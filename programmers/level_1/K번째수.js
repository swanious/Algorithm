function solution(array, commands) {
  var answer = [];
  commands.forEach((c) => {
    const [st, ed, idx] = c;
    const newArr = array.slice(st - 1, ed).sort((a, b) => a - b);
    answer.push(newArr[idx - 1]);
  });
  return answer;
}
