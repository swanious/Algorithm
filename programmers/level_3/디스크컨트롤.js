function solution(jobs) {
  let l = jobs.length;
  let totalTime = 0; // 총 시간
  let duration = 0; // 요청부터 종료까지 걸린 시간의 합
  let disk = []; // 작업 실행부 배열

  // 정렬이 된 배열이 주어진다는 조건이 없으므로, 시작시간 순서대로 오름차순 정렬
  jobs.sort((a, b) => a[0] - b[0]);

  // jobs나 disk(작업 실행부)에 작업이 있으면 반복
  while (jobs.length || disk.length) {
    // 작업이 있고, 첫 작업의 시작시간이 총 시간보다 작거나 같을 때 반복(예제처럼 한 작업의 종료시간 전에 시작하는 작업이 있을 때)
    while (jobs[0] && jobs[0][0] <= totalTime) {
      const temp = jobs.shift();
      disk.push(temp);
    }
    disk.sort((a, b) => a[1] - b[1]);
    if (disk.length) {
      const temp = disk.shift();
      // 총시간 = [이전의 총시간 + 소요시간]
      totalTime = totalTime + temp[1];
      // 요청부터 종료까지 걸린시간 = [총시간 - 현재 작업의 시작시간]
      duration += totalTime - temp[0];
    } else {
      // 만약 작업 사이에 텀이 있으면, 현재 작업의 시작시간으로 초기화
      // 예로, 이전 작업이 3ms에 끝났고, 새로운 작업이 4ms에 시작되면 totalTime을 4로 초기화
      totalTime = jobs[0][0];
    }
  }
  return Math.floor(duration / l);
}
