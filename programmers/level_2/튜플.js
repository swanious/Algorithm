function solution(s) {
  var answer = [];
  // { 가 있거나, }로 끝나는 정규표현식
  const regex = /\}$|\{/g
  
  // , 로 시작하는 정규표현식
  const regex2 = /^,/g
  
  // 정규표현식에 따라 새로운 배열 생성. 
  // 예시) {{20, 111}, {111}} 의 경우 ['20,111', '111', '']로 변경
  s = s.replace(regex, '');
  s = s.split('}')
  s.forEach((v,i) => {
      if (regex2.test(v)) {
          s[i] = v.replace(regex2, '')
      }
  })
  console.log(s)
  // s 배열의 맨 끝은 공백이므로 제거해주고 각 숫자마다 배열로 변환
  let newArr = s.slice(0, s.length-1);
  console.log(newArr)
  
  newArr.map((v, i) => {
      newArr[i] = v.split(',');
  })
  
  // 배열의 길이 기준으로 정렬한다.
  newArr.sort((a, b) => a.length - b.length)
  
  newArr.map((arr, i) => {
      arr.map(v => {
          if (!answer.includes(parseInt(v))) answer.push(parseInt(v))
      })
  })
  return answer;
}