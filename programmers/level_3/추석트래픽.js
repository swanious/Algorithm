/* 풀이과정
    밀리세컨 단위이기 때문에 첫 로그 시작부터 마지막 로그까지 스캔할 경우 (24 * 3600 * 1000 * n * 1000ms)만큼의 연산이 필요하기 때문에 해당 방식으로는 풀이가 불가능하다.
    
    요청량이 변하는 순간은 각 로그의 시작과 끝 뿐이므로 각 로그 별로 2번의 비교 연산을 수행하면 O(n^2)으로 풀이할 수 있다.
    1. 시작점과 끝점, 그리고 걸리는 시간을 각각 나눈다.
    2. (times배열) 범위를 판단하기 위해 배열에 시작점, 끝점을 삽입한다.
    3. (arr배열) 범위와 비교할 배열을 생성한다.
    4. 범위에 해당하는 로그의 수를 구한다.
*/
function solution(lines) {
  var arr = [];
  var times = [];

  for (var line of lines) {
    var temp = line.split(" ");

    var duration = temp[2].substring(0, temp[2].length - 1) * 1;
    var endTime =
      temp[1].substring(0, 2) * 3600 +
      temp[1].substring(3, 5) * 60 +
      temp[1].substring(6, 12) * 1;
    var startTime = endTime - duration + 0.001;

    // 비교를 위한 배열, 시작/종료 시간을 담은 배열
    arr.push([startTime, endTime]);
    times.push(startTime, endTime);
  }

  var maxCnt = 0;
  for (var i = 0; i < times.length; i++) {
    var working = 0;
    var stRange = times[i];
    var edRange = times[i] + 1; // 시작시간부터 1초 후까지 보기 위해

    for (var j = 0; j < arr.length; j++) {
      var st = arr[j][0];
      var ed = arr[j][1];

      // 1. 시작점이 범위에 포함될 때, 2. 끝점이 범위에 포함될 때, 3. 처음과 끝점 사이가 범위에 포함될 때
      if (
        (st >= stRange && st < edRange) ||
        (ed >= stRange && ed < edRange) ||
        (st <= stRange && ed >= edRange)
      )
        working++;
    }
    maxCnt = Math.max(maxCnt, working);
  }

  return maxCnt;
}
