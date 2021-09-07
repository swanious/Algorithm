function solution(people, limit) {
  var answer = 0;
  people.sort((a, b) => a - b);
  let i = 0, j = people.length - 1;
  while (i <= j) {
      if (i === j) {
          answer++;
          break;
      }
      if (people[i] + people[j] <= limit) {
          i++;
          j--;
      } else {
          j--;
      }
      answer++
  }

  return answer;
}