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