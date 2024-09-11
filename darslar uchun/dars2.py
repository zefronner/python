import os;os.system("cls")
"""
#11

# s = int(input("N: "))

# for i in range(1,s,1):
#     if i % 105 == 0:
#         print(i)

#12

# n = int(input("N: "))

# for i in range(1,n,):
#     if i % 24 == 0:
#         print(i)

#13

# n = 40; m = 180
# y = 0
# for i in range(n,m,1):
#     if i % 14 == 0 and i % 24 == 0:
#         y += i
# print("Yig'indisi: ",y)

#14

# n = int(input("Musbat son kiriting: "))
# s = 0
# while n > 0:
#     s += 1
#     n //= 10
# print(s)

#robocontest

# a,b,c,d,e = map(int, input("5 ta son kiriting: ").split())

# p = max(a,b,c,d,e)
# t = min(a,b,c,d,e)
# print(a+b+c+d+e - p)
# print(a+b+c+d+e - t)

# n = int(input())

# if n % 2 == 0:
#     print("Second player")
# else:
#     print("First player")

# a = int(input())
# b = int(input())
# print(b-a+1)

# a,b = map(int , input().split())

# print(a*b)

# a,b,c = map(int ,input().split())

# if a + b >= c:
#     print(a + b - c)
# else :
#     print("Error")

# n = int(input())

# if n % 2 == 0:
#     print(n * 2 + 1)
# else:
#     print(n * 2)

# n = int(input())
# k = 5 ; s = 0
# for i in range (n):
#     x = k // 2
#     s = s + x
#     k = x * 3
# print(s)

s = "salom"

for i in s:
    if i == 'a':
        continue
        print(i,end="")

soz = "Salom bolalar"

for i in range(len(soz)):
    print(soz[i])

soz = "Salom bolalar"
for i in range (len(soz)):
    if soz [i] == ' ':
        break
    print(i,end="")
s = input("Matn kiriting: ")
for i in s:
    if i.isdigit():
        i = 'A'
    print(i,end="")
# a,b,c = map(int , input().split())
# m = max(a,b,c)
# print(m)

# a,b = map(int,input().split())
# print(a*b)

# a = int(input())
# b,c,d = map(int,input().split())

# if d+b+c >= a:
#     print("Yes")
# else: 
#     print("No")

# a,b = map(int,input().split())
# print(b-(a*(b//a)))
n = int(input("N: "))

midlle = n / 2

for i in range(1,n+1):
    for k in range(n - i):
        print(end=" ")
    for j in range(1,i+1):
        print(end="* ")
    print()"""
a = int(input())
print(a**2)
