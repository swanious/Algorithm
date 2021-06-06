function solution(progresses, speeds) {
  var answer = [];
  var maxNumber = 0;
  var stackNumber = 0;

  for (var i = 0; i < progresses.length; i++) {
    var leftDays = Math.ceil((100 - progresses[i]) / speeds[i]); // 남은 날

    if (!maxNumber) {
      maxNumber = leftDays;
      stackNumber++;
      continue;
    }

    if (maxNumber >= leftDays) {
      stackNumber++;
      if (i === progresses.length - 1) {
        answer.push(stackNumber);
      }
    } else {
      answer.push(stackNumber);
      stackNumber = 1;
      maxNumber = leftDays;
      if (i === progresses.length - 1) {
        answer.push(stackNumber);
      }
    }
  }
  return answer;
}
