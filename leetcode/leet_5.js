/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  var i,
    len = Math.floor(s.length / 2) + 1,
    isTotalPalindrome = true;

  for (i = 0; i < len; i++) {
    if (s[i] != s[s.length - i - 1]) {
      isTotalPalindrome = false;
      break;
    }
  }

  if (isTotalPalindrome) return s;

  s = [].join.call(s, "#");
  s = "$#" + s + "#$";

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
