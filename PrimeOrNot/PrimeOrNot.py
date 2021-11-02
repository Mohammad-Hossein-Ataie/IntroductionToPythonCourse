number = int(input('please input your number: '))
if number > 1:
    for i in range(2,number//2):
        if (number % i) == 0:
            print('not prime')
            break
    else:
        print('prime')

else:
    print('not prime')
