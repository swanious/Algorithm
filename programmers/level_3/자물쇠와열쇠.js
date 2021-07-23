// 배열 90도 회전
const rotate90 = (arr) => {
  let temp = Array.from(Array(arr.length), () => Array(arr.length).fill(0));

  arr.forEach((row, y, arr) => {
    row.forEach((column, x) => {
      temp[y][x] = arr[arr.length - x - 1][y];
    });
  });
  return temp;
};

const check = (board, lockLength) => {
  const temp = Array.from(Array(lockLength), () =>
    Array(lockLength).fill(null)
  );
  for (let i = lockLength; i < lockLength * 2; i++) {
    for (let j = lockLength; j < lockLength * 2; j++) {
      if (board[i][j] !== 1) return false;
    }
  }
  return true;
};

function solution(key, lock) {
  const len = lock.length;

  // checkBoard 초기화 (예시 1 -> 9 * 9 배열을 생성)
  let checkBoard = Array.from(Array(len * 3), () => Array(len * 3).fill(null));
  for (let i = len; i < len * 2; i++) {
    for (let j = len; j < len * 2; j++) {
      checkBoard[i][j] = lock[i - len][j - len];
    }
  }
  for (let _ = 0; _ < 4; _++) {
    // key배열을 90도씩 4번 돌아가면서 check
    key = rotate90(key);

    for (let i = 0; i < checkBoard.length - key.length; i++) {
      for (let j = 0; j < checkBoard.length - key.length; j++) {
        // tempBoard를 초기화하고, board에 key를 맞춰보기(채워나가기)
        let tempBoard = [...checkBoard.map((v) => [...v])];
        for (let n = 0; n < key.length; n++) {
          for (let m = 0; m < key.length; m++) {
            tempBoard[i + n][j + m] += key[n][m];
          }
        }
        // key를 맞춰본 tempBoard를 순회하면서 자물쇠랑 열쇠랑 딱 맞으면 true 반환
        if (check(tempBoard, len)) return true;
      }
    }
  }
  // key랑 board랑 다 맞춰봐도 안되면 false 반환
  return false;
}
