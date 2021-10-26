laptop = int(input())
good_price = 0
for i in range(laptop):
    cost_vs_quality = input()
    cq_list = cost_vs_quality.split()
    for item in cost_vs_quality:
        while cq_list[0] < cq_list[1]:
            good_price += 1
            break
if good_price > 2:
    print("happy irsa")
else:
    print("poor irsa")
