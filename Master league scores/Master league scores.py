# Sepidrood team scores and wins
win = 0
total_score = 0
for i in range(30):
    score = int(input("Please enter the score: \n>>>"))
    total_score += score
    if score == 3:
        win += 1
print(total_score, win)
