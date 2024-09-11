import os;os.system("cls")
"""

# print("3 oydan so'ng")
# son = 123
# satr = "Satrga tegishli"
# b = True
# fson = 123321312.1321

# print(son,type(son))
# print(satr,type(satr))
# print(b,type(b))
# print(fson,type(fson))
# print("xayr" * 2)
# son = "nima"
# print(son,type(son))

text = "salom bolalar bugun havo juda issiq"
text2 = "Yashimisizlar"

print(text[1:5:1])
print(text[1: :1])
print(text[::1])
print(text[::-1])
print(text[12:1:-1])
print(end="\n\n")
print(text[::-2])

son=123;bol =True
fson = 123.123; soz = "salom"

print(f"int son{son}\nbool son {bol}")
print(f"float son{fson}\nstr qiymat {soz}")

print("int son {}\nbool qiymat {}".format(son,bol))
print("float son {}\nstr qiymat {}".format(fson,soz))

s = int (input("son: "))
b = s != 0
print(b)"""
"""a = int(input("A ==> "))
b = int(input("B ==> "))

a , b = b , a

print("Javob: ")

print(f"A ==> {a}") 
print(f"B ==> {b}")"""
"""print(1,2,3,4,5,sep="+",end=" = ")
print(1+2+3+4+5)

s = input("Matn kiriting: ")
print(*s,sep="*")

a,b, = map(int, input("Sonlarning kiriting: ").split())
c = (a + b) * 2
print("Perimetri: ",c)

a,b,c,d,e = map(int ,input("5 ta son kiriting: ").split())
y=0
b=0
if(a%2==0):
    y += a
    b += 1
if(b%2==0):
    y += b
    b += 1
if(c%2==0):
    y += c
    b += 1
if(d%2==0):
    y += d
    b+=1
if(e%2==0):
    y += e
    b+=1
y = y * 3  
b = y / b
print("O'rta arifmetigi: ",b)
soz = input("Matn: ")

if 'a' in soz:
    print("Bor")
else:
    print("Yo'q")
    
    
a = input("Son: ")

if '2' in a:
    print("bor")
else:
    print("yo'q")"""
son = 74
a = input("69 va 75 sonlari orasidagi sonni toping: ")
if a > son :
    print("sovuq")
elif a < son:
    print("Issiq")
else :
    print("To'g'ri|")

