/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
 var mergeKLists = function(lists) {
  var numberList = [];
  lists.forEach(item => {
      while (item && item.val !== null) {
          numberList.push(item.val);  // item.val은 [1,4,5] 중 1이 들어감
          item = item.next; // [1,4,5] -> [4,5] -> [5] -> null
      }
  })
  
  // 역순으로 정렬해줘야 LinkNode에 넣을 때 반대로 정렬됩니다.
  numberList = numberList.sort((a, b) => b - a) 
  
  let result = null;
  numberList.forEach(item => {
      let tempNode = new ListNode(item);
      tempNode.next = result;
      result = tempNode;  // [6 -> null] [5 -> 6 -> null] ... [1 -> 1 -> ... 5 -> 6 -> null]
      console.log(result)
  })
  return result
};