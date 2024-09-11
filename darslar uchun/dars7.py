import os; os.system("cls")
import sys
'''

def hisobla(a: int,b: int):
    try:
        natija = a / b
    except ZeroDivisionError:
        print("Nolga bo'sh mumkin emas!!")
    except TypeError:
        print("Bu int emas!!")
    else:
        print(natija)

hisobla(12,2)

serya = """Olam tush
            tarvuz pish
            qovun kesil"""

file = open("dars__7.txt" , "w")
file.write(serya)

lis = ["Kimdir" , "Nimadir" , "Qayerdir"]
file.writelines(lis)

for i in lis:
    file.write(i)
    file.write(" ")
file.close()

f = open("dars__7.txt","r")
matn = f.read()
print(matn,end="\n\n\n")

f.seek(0)
for i in f:
    for j in i:
        print(j,end="")

f.seek(0)
print()
text = f.readline()
print(text)
f.seek(0)

print()
print()
ls = f.readlines()
print(ls)


for i in ls:
    for j in i:
        print(j,end=" * ")
f.close()'''
f = open("soz.txt" , "r")
if f.readable():
    print("Fayldan ma'lumot o'qishingiz mumkin\n")
else:
    sys.exit("Sizga Fayldan malumot o'qishga ruxsat yo'q\n")
res , ls = [], []
data = f.read()
for i in data.split("\n"):
    ls.extend(i.split("."))
for j in ls:
    res.extend(j.split())
natija = sorted(res,key=len)

for i in natija:
    print(f"{i} >> {len(i)}")
print()
dic = {}
for i in natija:
    dic[i] = len(i)

print(dic)
print("Max >> ",natija[-1])
print("Min >> ",natija[0])

