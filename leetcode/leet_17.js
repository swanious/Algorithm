/*
17. Letter Combinations of a Phone Number
  Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

  A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

  var map = {
      '2' : ['a','b','c'],
      '3' : ['d','e','f'],
      '4' : ['g','h','i'],
      '5' : ['j','k','l'],
      '6' : ['m','n','o'],
      '7' : ['p','q','r','s'],
      '8' : ['t','u','v'],
      '9' : ['w','x','y', 'z'],
  }

  Example 1:

  Input: digits = "23"
  Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
  Example 2:

  Input: digits = ""
  Output: []
  Example 3:

  Input: digits = "2"
  Output: ["a","b","c"]
*/

// 기본적인 순열 풀이로 풀 수 있다.
var letterCombinations = function (digits) {
  var results = [];

  // digits이 비어있을 수도 있다.
  if (!digits.length) return results;

  var map = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
  };

  // 순열 함수
  function permute(str, index) {
    // 재귀 탈출 조건
    if (digits.length === index) {
      results.push(str);
      return;
    }
    // 순열
    else {
      for (const d of map[digits[index]]) {
        permute(str + d, index + 1);
      }
    }
  }
  permute("", 0);

  return results;
};

console.time("speed");
const answer = letterCombinations("7979");
console.log(answer);
console.timeEnd("speed");
