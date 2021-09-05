function solution(name) {
  const l = name.length;
  const arr = new Array(l).fill('A');
  let answer = 0;
  let min = name.length - 1;
  
  for (let i = 0; i < l; i++) {
      answer += getDistanceForNumber(name[i], arr[i]);
      
  }
  for (let i = 0; i < l; i++) {
      let idx = i;
      if (name[i] === 'A') {
          while (idx < name.length && name[idx] === 'A') {
              idx++
          }
          // 현재 idx는 연속된 A가 끝나는 idx이다.
          // (i-1) * 2는 해당 i까지 갔다가 뒤로 돌아가기 위함이다.
          // 예로, ABAAAB가 있을때 A -> B로 우측한칸 B -> A로 다시 돌아가기 위해 좌측한칸 => 2칸
          let moveCnt =  (i - 1) * 2 + name.length - idx;
          min = Math.min(moveCnt, min);
      }
  }
  return answer + min;
}

const getDistanceForNumber = (target, str) => {
  const targetIdx = target.charCodeAt() - 65;
  const strIdx = str.charCodeAt() - 65;
  const distance = Math.abs(targetIdx - strIdx)
  return distance > 13 ? Math.abs(distance - 26) : distance;
}
