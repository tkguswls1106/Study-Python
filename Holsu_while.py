count = int(input('반복횟수 입력: '))
print('홀수 출력 시작:')
i = 0  #while문이므로 i의 선언을 잊어서는 안됨.
while i<count:
        i+=1    #i가 0부터 시작하므로 1더하고 시작해도 문제없음.
                #뿐만아니라 count 숫자까지도 밑의 조건식에 넣어볼수도 있게됨.
        if i%2==0:
                continue
        print(i)
print('홀수 출력 끝!')
