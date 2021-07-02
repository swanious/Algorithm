function solution(begin, target, words) {
  // target이 words안에 없으면 0 반환
  if (!words.includes(target)) return 0;

  let answer = [];

  const dfs = (text, arr, count) => {
    let list = [...arr];
    let word = list.shift();

    // target을 찾으면 탈출
    if (word === target || list.length == 0) {
      if (check(text, word)) {
        answer.push(count + 1);
      }
      return;
    }

    if (check(text, word)) {
      dfs(word, list, count + 1);
    }

    dfs(text, list, count);
  };

  words.forEach((a, b, arr) => {
    let word = arr.shift();
    arr.push(word);

    dfs(begin, arr, 0);
  });
  // 찾았을 때의 count 중 가장 작은 값 뽑기
  return answer.length ? Math.min(...answer) : 0;
}

const check = (str1, str2) => {
  const l = str1.length;
  let count = 0;

  for (let i = 0; i < l; i++) {
    if (str1[i] === str2[i]) count++;
  }

  // 한글자 차이 ? true, 아니면 false
  return l - count === 1;
};
