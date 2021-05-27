function solution(record) {
  const log = [];
  const users = new Map(); // key:value 쌍으로 받아줄 Map 생성

  record.forEach((each) => {
    const [command, id, name] = each.split(" "); // 필요한 값들을 split으로 분리
    // 커맨드 별 조건에 따른 결과 저장
    if (command === "Enter") {
      users.set(id, name);
      log.push({ id, message: "님이 들어왔습니다." });
    }
    if (command === "Change") users.set(id, name); // 변경이 일어날 경우 존재하는 id에 새로운 value를 넣어주면 변경
    if (command === "Leave") log.push({ id, message: "님이 나갔습니다." });
  });

  return log.map((each) => {
    return `${users.get(each.id)}${each.message}`;
  });
}
