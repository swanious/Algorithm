/**
 * @param {number[]} height
 * @return {number}
 */

// 투포인터를 사용한 풀이
// runtime-136 ms  memory-48 MB
var maxArea = function (height) {
  var i = 0,
    j = height.length - 1,
    maxV = 0;

  while (i <= j) {
    maxV = Math.max(maxV, (j - i) * Math.min(height[i], height[j]));
    if (height[i] <= height[j]) {
      i++;
    } else {
      j--;
    }
  }
  return maxV;
};
