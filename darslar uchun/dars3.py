import os; os.system("cls")
import math as m
"""
a = [1,2,3,4,5]
b = list()

print(*a)

print(a[4]) 
for i in a:
    print(i,end=" ")

print()

for i in range(len(a)):
    print(a[i],end=" ")
a = ["Salom" , True, 123,234.23,"akmal",False]

for i in range(len(a)):
    if type(a[i]) == str or type(a[i]) == bool:
        print(a[i])
b = list()
b.append(123)

print(len(b))
n = int(input("N: "))
for i in range(n):
    k = input()
    b.append(k)
print(b)

print(len(b))"""
"""b = list()
 #! append
b = ["salom",12,True]
print(b)
b.append(1232.123)
print(b)

#! insert
b.insert(0,"Mana_sanga")
print(b)
b.insert(2, False)
print(b)

#! remove
b.remove(12)
print(b)
b.remove("salom")
print(b)

#! pop

b.pop(2)
print(b)
d = b.pop()
print(d)
print(b)"""
ls = [2 , 1]
while True:
    print("\tMa'lumot\n")
    print("0)Dasturni yakunlash")
    print("1)Mavjud ma'lumot ko'rish")
    print("2)Ma'lumot qo'shish")
    print("3)Ma'lumot o'chirish")
    print("4)Ma'lumotlarni so'rtlash")
    print()
    k = int(input("Tanlash:"))
    print()
    if k == 0:
        break
    elif k == 1:
        print(ls)
    elif k == 2:
        print("\tMa'lumot qo'shish turlari.")
        print("1)Oxiridan bitta qo'shish")
        print("2)Indexiga qo'shish")
        print("3)Oxiriga qo'shish")
        print()
        y = int(input("Tanlash: "))
        if y == 1:
            qoshish = int(input("Qo'shish uchun ma'lumot kiriting: "))
            ls.append(qoshish)
        elif y == 2:
            qoshish = int(input("Qo'shish uchun ma'lumot kiriting: "))
            index = int(input("Index: "))
            ls.insert(index,qoshish)
        elif y == 3:
            qoshish = int(input("Bir nechta ma'lumotni bo'sh joy bilan ajratib kiriting: "))
            ls.extend(qoshish.split()) 
    elif k == 3:
        print("\tMa'lumot o'chirish turlari.")
        print("1)Remove orqali")
        print("2)Pop orqali")
        print("3)Clear orqali")
        print()
        o = int(input("Tanlash:"))
        if o == 1:
            print("O'chirilishi krk bo'lgan ma'lumotni kiriting: ")
            ochir = int(input())
            ls.remove(ochir)
        elif o == 2:
            ochir = int(input("Ma'lumot indexini kiriting: "))
            ls.pop(ochir)
        elif o == 3:
            ls.clear()
    elif k == 4:
        print("\tMa'lumot so'rtlash turlari.")
        print("1)To'g'ri")
        print("2)Teskari sort")
        print("3)Teskari aylantirish")

        p = int(input("Tanlash: "))

        if p == 1:
            ls.sort()
        elif p == 2:
            ls.sort(reverse="True")
        elif p == 3:
            ls.reverse()