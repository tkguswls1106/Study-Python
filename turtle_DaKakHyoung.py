import turtle as t
n= int(input('몇각형의 도형을 원하십니까?: '))

t.shape('turtle')
t.color('red')
t.begin_fill()  #색칠할 영역 시작
for i in range(n):
        t.forward(100)
        t.right(360/n)
t.end_fill()  #색칠할 영역 끝
