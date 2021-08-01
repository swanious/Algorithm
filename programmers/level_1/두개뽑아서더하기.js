function solution(numbers) {
  var answer = new Set();
  for (let i = 0; i < numbers.length; i++) {
      for (let j = i + 1; j < numbers.length; j++) {
          const sum = numbers[i] + numbers[j];
          if (!answer.has(sum)) answer.add(sum);
      }
  }
  return [...answer].sort((a, b) => a - b);
}