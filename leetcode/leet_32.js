/**
 * @param {string} s
 * @return {number}
 */
 var longestValidParentheses = function(s) {
  s = s.split('');
  var maxAns = 0;
  var stack = [];
  // 처음에 ()가 나올 경우 1-(-1) = 2로 결과가 나와야하므로,
  stack.push(-1);
  s.forEach((v, i) => {
    if (v === '(') {
        stack.push(i)
    } else {
        stack.pop();
        if (stack.length === 0) {
            stack.push(i)
        } else {
            maxAns = Math.max(maxAns, i - stack[stack.length - 1])
        }
    }
  })
  
  return maxAns;
};