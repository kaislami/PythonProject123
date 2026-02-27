import random
N=int(input("Kuinka monta pistettä arvotaan: "))
ympyra= 0
for i in range (N):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x**2+y**2<1:
        ympyra+=1
pi=4*ympyra/4
print("Piin likiarvo on:", pi)
