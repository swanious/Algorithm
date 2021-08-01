function solution(s) {
  const obj = { zero:0, one:1, two:2, three:3, four:4, five:5, six:6, seven:7, eight:8, nine:9 }
  var answer = '';
  var newArr = [...s];
  let tempStr = '';
  newArr.forEach((v, i) => {
      if (isNaN(v)) {
          tempStr += v
          if (Object.keys(obj).includes(tempStr)) {
              answer += obj[tempStr].toString()
              tempStr = ''; // 초기화
          };
      }
      
      else answer += v
  })
  return parseInt(answer);
}