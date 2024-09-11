import os; os.system("cls")
'''
def salom():
    print("salom")
def hayr():
    print("Qaytib kema")
salom()
hayr()

def qosh(a,b):
    return a+b
print(qosh(12,23))
def daraja(a,b,c):
    return"""
    {} darajasi {}
    {} darajasi {}
    {} darajasi {}""".format(a,a**a,b,b**b, c,c**c)

a,b,c = map(int,input(">> ").split())
c = daraja(a,b,c)
print(c,type(c))

def prod(dic):
    k = dic.values()
    p = max(k)
    print(p)
soni = int(input("soni >> "))
dic = {}
for i in range(soni):
    k = input("key >> ")
    v = input("value >> ")
    dic[k] = v
prod(dic)'''
def tub(ls ):
    b = 0
    j = 1
    op = []
    for i in ls:
        if i%j==0:
            b+=1
            op.append(i)
        j+=1
    print(op)
ls = [2,3,4,5,6,7,8,9,11,13]
tub(ls)