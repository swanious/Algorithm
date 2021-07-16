function solution(new_id) {
  var answer = "";
  // 1단계- 대문자있으면 모두 소문자로 변환
  answer = new_id.toLowerCase();
  // 2단계- 소문자, 숫자, -_. 을 제외한 모든 문자 제거
  answer = answer.replace(/[^a-z0-9-_.]+/g, "");
  // 3단계- (..) -> (.) 변환
  answer = answer.replace(/\.\.+/g, ".");
  // 4단계- 마지막에 마침표(.)있으면 제거
  answer = answer.replace(/^\.|\.$/g, "");
  // 5단계- 빈 문자열이면 'a' 대입
  if (answer === "") answer = "a";
  // 6단계- 길이가 16자 이상이면 15개로 변환 후 끝에 (.)있으면 제거
  if (answer.length > 15) {
    answer = answer.substr(0, 15);
    answer = answer.replace(/\.$/g, "");
  }
  // 7단계- 길이가 2자 이하면 3자가 될 때까지 마지막 문자 더해주기
  while (answer.length < 3) {
    answer = answer + answer[answer.length - 1];
  }
  return answer;
}
