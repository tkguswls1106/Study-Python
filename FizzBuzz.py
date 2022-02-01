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
