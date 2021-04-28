import sys
import re  # 정규표현식 내장 함수 사용

n = int(input())
result = []
for i in range(n):
    s = input()

    # 표현식을 compile한 후, 입력값과 비교한다.
    # match의 흐름은 다음과 같다.
    '''
    p = re.compile(정규표현식)
    m = p.match( 'string goes here' )
    if m:
        print('Match found: ', m.group())
    else:
        print('No match')
    '''
    
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(s)
    if m:
        result.append('YES')
    else:
        result.append('NO')
for i in result:
    print(i)
