function solution(table, languages, preference) {
  const tableObj = { 0: 'CONTENTS', 1: 'GAME', 2: 'HARDWARE', 3: 'PORTAL', 4: 'SI' }; // 사전순 출력을 위한 Obj
  const prefObj = {}; // 언어 선호도
  const scores = new Array(table.length).fill(0); // 점수 총합 배열
  table = table.sort() // 사전순 정렬
  
  for (let i = 0; i < languages.length; i++) {
      prefObj[languages[i]] = preference[i] ;
  }
  
  table.forEach((row, idx) => {
      const lang = row.split(' ').slice(1).reverse(); // 점수를 인덱스 순으로 저장하기 위해 뒤집어줌 (5, 4, 3, 2, 1 => 1, 2, 3, 4, 5)
      lang.map((v, i) => {
          // 언어 선호도가 있는 언어이면 score올려주기
          if (languages.includes(v)) scores[idx] += prefObj[v] * (i + 1);
      })
  })
  
  return tableObj[scores.indexOf(Math.max(...scores))];
}