/*
  종류의 개수를 구하면 되므로 중복을 제거하기 위해 new Set()을 사용하여 해결할 수 있다.
*/
function solution(nums) {
  var limit = Math.floor(nums.length / 2);
  var numsSet = new Set();

  for (var n of nums) {
    numsSet.add(n);
  }

  // 종류의 개수가 n/2보다 적으면 종류의 개수 리턴
  if (limit > numsSet.size) return numsSet.size;
  // 아니면 n/2 리턴
  else return limit;
}
