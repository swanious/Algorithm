var maxSlidingWindow = function(nums, k) {
  // 초기값
  var array = nums.slice(0, k); // 초기 배열
  var maxVal = Math.max(...array); // 초기 max값
  var maxValArr = [maxVal]; // 결과 배열
  var tempLeft;
  var tempRight;
  
  for (var i = 1; i< nums.length - k + 1; i++) {
      // 왼쪽 shift값, 오른쪽 push값
      tempLeft = array.shift();
      tempRight = nums[i + k - 1];
      array.push(tempRight);
      
      if (tempRight >= maxVal) {
          maxVal = tempRight;
          maxValArr.push(maxVal);
      } else {
          if (tempLeft === maxVal) {
             maxVal = Math.max(...array);
             maxValArr.push(maxVal);
          } else if (tempLeft < maxVal) {
              maxValArr.push(maxVal)
          }
      }
  }
  return maxValArr;
};