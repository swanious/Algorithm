/** 
    의상은 무시해도 됨(같은 이름을 가진 의상 x)
    무조건 한 개 이상은 입음(모든 조합 - 1)
    
    ex)
    1. 
    예시처럼 모자 2개, 안경 1개일 경우, 
    3 * 2 - 1 =  5(가지 조합)이 가능해야함. 
    그래서 아래처럼 초기값을 1이 아닌 2로 해줌.
    obj는 { headgear: 3, eyewear: 2 }
    
    2.
    종류가 모자, 안경, 상의 각각 3개일 경우
    2 * 2 * 2 - 1 = 7(가지 조합)
    obj는 { headgear: 2, eyewear: 2, shirt: 2 }
*/ 
function solution(clothes) {
  let obj = clothes.map(v => v[1]).reduce((acc, cur) => {
      if (acc[cur]) acc[cur]++;
      else acc[cur] = 2;
      return acc
  }, {})
  console.log(obj)
  return Object.values(obj).reduce((acc, cur) => acc * cur, 1) - 1;
}
