const stdin = require("fs")
  .readFileSync("test.txt", "utf-8")
  .trim()
  .split("\n");

const input = (() => {
  let l = 0;
  return () => stdin[l++];
})();

const bSearch = (arr, num) => {
  let left = 0;
  let right = arr.length;

  while (left < right) {
    let mid = Math.floor((left + right) / 2);
    if (arr[mid] > +num) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }

  return right;
};

const T = +input();
for (let tc = 0; tc < T; tc++) {
  const N = +input();
  const arr = [];
  const count = {}; // counting obj

  for (let i = 0; i < N; i++) {
    const [cmd, num] = input().split(" ");
    if (cmd === "I") {
      // 카운트가 존재하면 값을 찾을필요가 없음
      if (count[num]) {
        count[num]++;
      }
      // 해당 값이 존재하지 않을때만 삽입
      else {
        const idx = bSearch(arr, +num);
        arr.splice(idx, 0, +num);
        count[num] = 1;
      }
    } else {
      // arr가 없으면 무시
      if (!arr.length) continue;

      // 최솟값을 뺄 때
      if (+num === -1) {
        // 값이 중복일 때는 그냥 count만 빼줌
        if (count[arr[0]] > 1) {
          count[arr[0]]--;
        }
        // 값이 한개 밖에 없을때는 정렬된 배열의 첫번째 값을 빼준다.
        else {
          delete count[arr[0]];
          arr.shift();
        }
      }
      // 최댓값을 뺄 때
      else {
        // 값이 중복일 때는 그냥 count만 빼줌
        if (count[arr[arr.length - 1]] > 1) {
          count[arr[arr.length - 1]]--;
        }
        // 값이 한개 밖에 없을때는 정렬된 배열의 첫번째 값을 빼준다.
        else {
          delete count[arr[arr.length - 1]];
          arr.pop();
        }
      }
    }
  }

  arr.length > 0
    ? console.log(`${arr[arr.length - 1]} ${arr[0]}`)
    : console.log("EMPTY");
}
