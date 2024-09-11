import os; os.system("cls")
"""
l1 = [int(input()) for i in range(int(input("N1: ")))]
l2 = [int(input()) for i in range(int(input("N2: ")))]
l3 = [int(input()) for i in range(int(input("N3: ")))]
l4 = [int(input()) for i in range(int(input("N4: ")))]

l = [l1,l2,l3,l4]

print(l) ; katta = 0
for i in l:
    if sum(i) > katta:
        katta = sum(i)

for j in l:
    if sum (j) == katta:
        print(j)"""

"""lst = [(),(),('',),(),('a','b'),(),('a','b','c'),(),('d')]

for i in range(lst.count(())):
    lst.remove(())
print(lst)

d = {1: 100 , 2: 200}
print(d)

n = int(input("Ma'lumot kiriting: "))

for i in range(n):
    f = input(f"{i} - key >> ")
    r = input(f"{i} - value >> ")
    d[f] = r
print(d)"""
d = {1: "Salom" , 2: "aziz"}
d = d.items()
print(d)
for i in d:
    i = list (i)
    if len(i) == 5:
        print(d[i])