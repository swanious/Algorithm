/**
 * @param {string} s
 * @return {string}
 */

/*
  가장 긴 팰린드롬 찾기

  시간복잡도 O(n)으로 풀기 위해서, Manacher's algorithm을 활용하여 풀이를 한다.
  http://www.secmem.org/blog/2019/03/10/Manacher/ 참고해보자.
*/
var longestPalindrome = function (s) {
  var i,
    len = Math.floor(s.length / 2) + 1,
    isTotalPalindrome = true;

  // 문자열 그 자체가 팰린드롬인 경우 그냥 s를 return 한다.
  for (i = 0; i < len; i++) {
    if (s[i] != s[s.length - i - 1]) {
      isTotalPalindrome = false;
      break;
    }
  }

  if (isTotalPalindrome) return s;

  // manacher's algorithm은 짝수는 판단할 수 없기에 문자열 중간에 판단할 수 있는 문자를 삽입하여 짝수도 판단가능
  s = [].join.call(s, "#");
  s = "$#" + s + "#$";

  // 각 A의 원소 A[i]는 i번째 문자열을 중심으로 하는 가장 긴 팔린드롬의 반지름의 길이.
  // 즉, S[(i−A[i])⋯(i+A[i])]는 팔린드롬이며, S[(i−A[i]−1)⋯(i+A[i]+1)]은 팔린드롬이 아니다.
  var A = [],
    C = 1,
    R = 1,
    iMirror,
    max = 0,
    maxIndex;

  for (i = 1; i < s.length - 1; i++) {
    iMirror = 2 * C - i;
    A[i] = R > i ? Math.min(R - i, A[iMirror]) : 1;

    while (s[i - A[i]] == s[i + A[i]]) A[i]++;

    if (i + A[i] > R) {
      R = i + A[i];
      C = i;
    }

    if (A[i] > max) {
      max = A[i];
      maxIndex = i;
    }
  }

  return s.substr(maxIndex - max + 1, 2 * max - 1).replace(/[#$]/g, "");
};
