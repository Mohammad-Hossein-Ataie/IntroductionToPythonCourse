# this code is written by Ali Esmaeilzadeh
# for Jadi's python course
candidates = []
while True:
    age = int(input())
    candidates += [age]
    first_maximum = max(candidates)
    if age == -1:
        # let's sort the list(min to max)
        sorted_candidates = (sorted(candidates))
        # The second item from the bottom of the list is the second maximum
        second_max = (sorted_candidates[-2])
        print(first_maximum, "", second_max)
        break
