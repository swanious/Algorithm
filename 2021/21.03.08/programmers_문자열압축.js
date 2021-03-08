function solution(s) {
    var answer = 9999999999;
    
    function sliceStr(string, n) {
        let li = [];
        let k = 0;
        while (string.slice(k, n + k)) {
            li.push(string.slice(k, n + k))
            k += n
        }
        return li
    }
    
    for (let i = 1; i < s.length / 2 + 1; i++) {
        let newList = sliceStr(s, i)
        let result = s.length // 압축을 안할때 결과 값
        let count = 0;
        for (let j = 1; j < newList.length; j++) {
            if (newList[j] === newList[j - 1]) {
                count += 1
            } else {
                if (count) {
                    result = result + ((count + 1).toString().length) - (count * i)
                    count = 0
                }
            }
        }
        if (count) {
            result = result + ((count + 1).toString().length) - (count * i)
        }
        answer = Math.min(result, answer)
        
    }
    
    if (answer === 9999999999) {
        answer = 1
    }
    return answer;
}