# function for divisors of a number:
def divisor(x):
    divisors = 0
    for i in range(1, x+1):
        if x % i == 0:
            divisors += 1
    return divisors


max_divisors = 0
count = 0
for i in range(20):
    number = int(input())
    if divisor(number) > count:
        max_divisors = number
        count = divisor(number)
    if divisor(number) == count and number > max_divisors:
        max_divisors = number
print(max_divisors, '', count)
