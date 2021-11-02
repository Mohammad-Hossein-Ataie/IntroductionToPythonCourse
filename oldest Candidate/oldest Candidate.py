candidates = []
while True:
    age = int(input())
    candidates += [age]
    maximum_age = max(candidates)
    if age == -1:
        print(maximum_age)
        break

