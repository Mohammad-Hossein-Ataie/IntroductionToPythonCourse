x=int(input())
dic={ }
for i in range(0,x):
	vaje=input()
	vaje=vaje.split(" ")
	dic[vaje[0]]=vaje[1]
jomle=input()
jomle=jomle.split(" ")
jomle1=[ ]
for vaje in jomle:
	jomle1.append(dic.get(vaje,vaje))
print(' '.join(jomle1))