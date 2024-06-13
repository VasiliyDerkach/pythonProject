class Buiding:
    total= 0
    def __init__(self):
        Buiding.total+= 1
VBuiding= []
for i in range(1,41):
    a= Buiding()
    VBuiding.append(a)
    print('N=',i, a)
print('Итог ',Buiding.total)
