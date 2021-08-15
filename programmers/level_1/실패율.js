function solution(N, stages) {
  const obj = {}; // 실패율을 담아줄 객체
  let answer = [];
  let l = stages.length;
  
  // 1...N 객체 초기화
  for (let i = 1; i < N + 1; i++) {
      obj[i] = 0
  }
  // stage의 개수를 세줄 객체
  const cntObj = stages.reduce((acc, cur) => {
      if (!acc[cur]) acc[cur] = 1;
      else acc[cur]++;
      return acc;
  }, {})
  
  // 실패율 구하기
  Object.entries(cntObj).map(v => {
      if (obj[v[0]] === 0) {
          obj[v[0]] = v[1] / l;
          l -= v[1]    
      }
      
  })
  // 역순으로 정렬해서 결과 반환
  const result = Object.entries(obj).sort((a, b) => b[1] - a[1]);
  result.map(v => answer.push(v[0] * 1))
  return answer;
}