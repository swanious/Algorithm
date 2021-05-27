/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */

// 그냥 조건문으로 풀어내기 보다 재귀를 사용해서 풀면 쉽게 풀 수 있다. 
// Discuss게시판에서는 RegExp 2줄짜리 코드도 봤다..)

var isMatch = function(s, p) {
      // 재귀탈출 조건 - 패턴이 끝까지 이동했을 때, s의 길이값으로 답을 판단한다.
      if (p.length === 0) {
          return s.length === 0;
      }
      // 첫 문자가 맞는지 여부
      var isFirstMatch = s.length > 0 && (s[0] === p[0] || p[0] === '.')
      
      // 패턴의 길이가 2보다 크고, 패턴의 다음 문자가 *이면,
          // 둘의 문자가 매치가 안되면 2칸 건너뛰고,
          // 둘의 문자가 매치되면 s를 한칸씩 옮기기
      if (p.length >= 2 && p[1] === '*') {
          return isMatch(s, p.substring(2)) || (isFirstMatch && isMatch(s.substring(1), p)) 
      } 
      // 둘이 매치되면 한칸씩 옮기기
      else {
          return isFirstMatch && isMatch(s.substring(1), p.substring(1))
      }
      
  };


// 이런 풀이도 가능하다. 정규표현식은 아직 잘 모르겠다... 공부해보는걸로..!
// var isMatch = function(s, p) {
//     let regex = new RegExp(p); // regex -> /.*/
//     return s.match(regex) ? s === s.match(regex)[0] : false;
// };
