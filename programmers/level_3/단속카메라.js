/** 
* 1. 진출 지점을 기준으로 정렬한다. 
* 2. A의 진출지점과 이외의 진입지점을 비교한다.
* 3. A의 진출지점보다 진입지점이 더 작은 차량은 단속카메라에 찍혔으므로, 배열에서 제거한다.
* 4. 위의 2, 3을 반복한다.
*/

function solution(routes) {
  // 빨리 나가는 순서대로 정렬    
  routes.sort((a, b) => a[1] - b[1]);
  let answer = 0;
  
  while (routes.length > 0) {
      const exitPosition = routes[0][1];
      
      for (let i = 0; i < routes.length; i++) {
          if (exitPosition >= routes[i][0]) {
              routes.splice(i, 1);
              i--
          }
      }
      answer++
  }
  return answer;
}