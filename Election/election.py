ara_list=[ ]
ara_dic={ }
tedad=int(input())
for i in range(0,tedad):
	ara_list.append(input())

for item in ara_list:
	if item in ara_dic.keys():
		ara_dic[item]+=1
	else:
		ara_dic[item]=1
asami=list(ara_dic.keys())
asami=sorted(asami)
for h in asami:
	print(h,' ',ara_dic[h])
	