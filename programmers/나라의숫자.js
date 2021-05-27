function solution(n) {
  var answer = '';
  var share = n;
  var remainder = -1;
  while (share !=0) {
      remainder = share % 3;
      share = Math.floor(share / 3);
      console.log(share, remainder)
      if (remainder == 0) {
          answer = "4" + answer
          share--
          console.log(answer)
      }
      else if (remainder == 1) {
          answer = "1" + answer
      }
      else if (remainder == 2) {
          answer = "2" + answer
      }
  }
  return answer;
}


/**
 * 정확성은 all pass
 * 효율성은 all fail
 * 인수분해를 하지않고 바로 값을 구할 수 있는 방법이 있을지 찾아보자.
 */

// 아래의 풀이로 all pass했다.

function solution(n) {
  var answer = '';
  var numberList = [4, 1, 2]; // 3으로 나누어떨어지면 4, 아니면 1, 2 순서대로 돌아간다.
  
  while (n) {
      /*
          ex)
          직접 넣어보면 이해가 간다.
          n이 12일 때,
          <첫번째>
          answer = 4 + '';
          n = 3
          <두번째>
          answer = 4 + '4';
          n = 0
          <정답>
          '44'
      */
      answer = numberList[n % 3] + answer;
      n % 3 === 0 ? n = Math.floor(n/3) - 1 : n = Math.floor(n/3)
  }
  return answer;
}