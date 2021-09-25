// 참고 - https://deok2kim.tistory.com/122

function solution(distance, rocks, n) {
  let start = 0;
  let end = distance;
  let answer = 0;

  rocks.sort((a, b) => a - b);

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    let removeCnt = 0;
    let currentPos = 0;

    for (let i = 0; i < rocks.length; i++) {
      if (rocks[i] - currentPos < mid) {
        removeCnt++;
      } else currentPos = rocks[i];
    }

    if (removeCnt > n) {
      end = mid - 1;
    } else {
      start = mid + 1;
      answer = mid;
    }
  }
  return answer;
}
