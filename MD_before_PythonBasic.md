# [파이썬 도장깨기 강의 시청전 Python 기초 공부 부분]

**이전 단계 기초 배운 Python 강의 영상 사이트 (현재 1:22:30 까지 시청완료): https://www.youtube.com/watch?v=kWiCuklohdY&t=4950s**
```
<#는 출력값을 적어둠>

문장들 마우스로 드래그하고 ctrl+/ 하면 해당 문장들이 전부 주석처리됨.

터미널 코드에 cls 입력하면 복잡하게 적혀있는것들 깔끔하게 전부 사라짐.

print(3>10)  #False
print(3<10)  #True
print(3==3)  #True
print(4==3)  #False
print(3 + 4 == 7)  #True
print(1 != 3)  #True
print(not(1 != 3))  #False
print((3>0) and (3<5))  #True
print((3>0) & (3<5))  #True
print((3>0) or (3>5))  #True
print((3>0) | (3>5))  #True

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3
print("우리집" + animal + "의 이름은 " + name + "예요")  #우리집강아지의 이름은 연탄이예요
print(name + "는", str(age) + "살이며, " + hobby + "을 아주 좋아해요")  콤마(,)는 출력할때 띄어쓰기 자동으로 해준다. #연탄이는 4살이며, 산책을 아주 좋아해요
print(name + "는 어른일까요? " + str(is_adult))  #연탄이는 어른일까요? True
print(name + "는 어른일까요?", str(is_adult))  #연탄이는 어른일까요? True

number += number 사용가능
-= 사용가능
*= 사용가능
/= 사용가능
%= 사용가능

print(2**3) 이거는 2의3제곱(승)을 프린트하라는 의미임.  #8
print(5/3) 이거는 5를 3으로 나누었을때의 값을 프린트하라는 의미임.  #1.6666666666666667
print(5//3) 이거는 5를 3으로 나누었을때의 몫 값을 프린트하라는 의미임.  #1
print(5%3) 이거는 5를 3으로 나누었을때의 나머지 값을 프린트하라는 의미임.  #2

print(abs(-5)) 이거는 -5의 절댓값을 출력하라는 의미임.  #5
print(pow(4, 2)) 이거는 4의2제곱 값을 출력하라는 의미임.  #16
print(max(5,12)) 이거는 5와 12중 최대값(둘중 더 큰값) 출력하라는 의미임.  #12
print(min(5,12)) 이거는 5와 12중 최솟값(둘중 더 작은값) 출력하라는 의미임.  #5
print(round(3.14)) 이거는 3.14를 반올림한 값을 출력하라는 의미임. #3

from math import *
print(floor(4.99))  4.99 소수점 내림  #4
printf(ceil(3.14))  3.14 소수점 올림  #4
print(sqrt(16))  16의 제곱근  #4.0

from random import *
print(random())  0.0 ~ 1.0 미만의 랜덤숫자 출력
print(random() * 10)  0.0 ~ 10.0 미만의 랜덤숫자 출력
print(random() + 1)  1.0 ~ 10.0 이하의 랜덤숫자 출력
print(int(random()))  0.0 ~ 1.0 미만의 랜덤숫자를 정수형으로 출력
print(randrange(1, 45))  1~45 미만의 랜덤숫자를 출력
print(randint(1, 45))  1~45 이하의 랜덤숫자를 출력

sentence = '가나다라 마바사'  사용가능함.
sentence2 = "가나다라 마바사"  사용 가능함.

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)  #나는 소년이고,(엔터)파이썬은 쉬워요

jumin = "001106-3111111"
print("성별: " + jumin[7])  #성별: 3
print("생년월일: " + jumin[0:6])  인덱스0부터6직전까지(0~5) 출력 / 같은말은 print("생년월일: " + jumin[:6])  #생년월일: 001106

python = "AbCdEFG"
print(python.lower())  전부 소문자로 출력  #abcdefg
print(python.upper())  전부 대문자로 출력  #ABCDEFG
print(python[0].isupper())  인덱스0의 문자가 대문자가 맞는가?  #True
print(len(python))  변수 python의 길이를 출력  #7
print(python.replace("AbC", "qwe"))  python 변수에서 AbC를 qwe로 변환하여 출력  #qwedEFG

str = "asdf zaca"
index = str.index("a")  str 변수에서 a가 들어있는 인덱스 찾기 / 없으면 에러나면서 프로그램 바로 종료시킴 / 바로 프린트에 넣지말고 이렇게 변수에 넣어주고 다음줄에 프린트하기. 안좋은예로 print(str.index("a"))
print(index)  #0
index = str.index("a", index+1)  str 변수에서 a가 들어있는 그다음 인덱스 찾기
print(index)  #6
find = str.find("a")  str 변수에서 a가 들어있는 인덱스 찾기 / 없으면 -1 출력하고 그 다음줄 코드 이어서 실행함 / 바로 프린트에 넣지말고 이렇게 변수에 넣어주고 다음줄에 프린트하기. 안좋은예로 print(str.find("a"))
print(find)  #0
print(str.count("a"))  str 변수에서 a가 몇번 들어가는지 숫자 출력  #3

print("나는 %d살 입니다." %22)  헷갈려서 실수로 큰따옴표 다음에 콤마(,) 붙이지말자  #나는 22살 입니다.
print("나는 %s을 좋아해요." %"파이썬")  #나는 파이썬을 좋아해요.
print("나는 %s과 %s를 좋아해요." %("파이썬", "C언어"))  #나는 파이썬과 C언어를 좋아해요.

print("나는 {}살 입니다.".format(22))  #나는 22살 입니다.
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))  #나는 파란색과 빨간색을 좋아해요.
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))  #나는 파란색과 빨간색을 좋아해요.
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))  #나는 빨간색과 파란색을 좋아해요.
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 22, color = "파란"))  #나는 22살이며, 파란색을 좋아해요.
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "파란", age = 22))  #나는 22살이며, 파란색을 좋아해요.

age = 22
color = "파란"
print(f"나는 {age}살이며, {color}색을 좋아해요.")  #나는 22살이며, 파란색을 좋아해요.  // f는 포맷팅(formatting) 약자이다.

\n은 문장내에서 출력할때 엔터를 쳐준다.

\"와 \'는 문장내에서 따옴표로 사용이 가능하다.
print('저는 "사현진"입니다.')  #저는 "사현진"입니다.
print("저는 \"사현진\"입니다.")  #저는 "사현진"입니다.
print("저는 \'사현진\'입니다.")  #저는 '사현진'입니다.

\\는 문장내에서 \로 출력된다.
print("C:\\Users\\user\\Desktop\\PythonWorkspace>")  #C:\Users\user\Desktop\PythonWorkspace>

\r은 커서를 맨앞으로 이동시켜준다.
print("ReddApple\rPine")  ReddApple을 적고 커서를 다시 앞으로가서 앞에서부터 글자수만큼 잘라내기식으로 Pine을 입력하여 출력해준다.  #PineApple

\b는 백스페이스로 지우는 역할을 해준다.
print("Redd\bApple")  #RedApple

\t는 탭 역할을 한다.
print("abc\tdef")  #abc     def

```
