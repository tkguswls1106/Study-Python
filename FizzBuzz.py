# <FizzBuzz문제 (3과 5의 배수 문제)>

for i in range(1, 101):
        if i%3==0 and i%5==0:
                print('FizzBuzz')
        elif i%3==0:
                print('Fizz')
        elif i%5==0:
                print('Buzz')
        else:
                print(i)

# 위의 긴 코드들을 짧은 코드로 단축시키면
# for i in range(1, 101):
#         print('Fizz' * (i%3==0) + 'Buzz' * (i%5==0) or i)
