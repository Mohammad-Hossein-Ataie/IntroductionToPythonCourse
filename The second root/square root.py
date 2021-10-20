# Ali ESmaeilzadeh
# jadi python course
import math
n = int(input())
s_r = []

for number in range(n):
    num = float(input())
    if num > 0:  # to avoid any error when user input a negative value
        s_r += [("{:.4f}".format(math.sqrt(num)))]

for i in s_r:
    print(i)
