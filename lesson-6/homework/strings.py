---


n = int(input('Enter any number: '))
for i in range(0, n):
    print(i**2)

a = 1
while a<11:
    print(a)
    a+=1

a = 5
for i in range(1, a+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

b = int(input('Enter any number: '))
total = 0
for i in range(1,b+1):
    total+=i
print(total)

a = 10
for i in range(1, a+1):
    print(i*2)

n = '75869'
print(len(n))

n =5
for i in range(n, 0, -1):
    for j in  range(i, 0, -1):
        print(j, end=' ')
    print()

list1 = [10, 20, 30, 40, 50]
print(list1[::-1])

start, end=-10, 0
for i in range(start, end):
    print(i)

n = 4
for i in range(0,n+1):
    print(i)
    if i==n:
        print('Done!')

start = 25
end = 50
for number in range(start, end):
    for num in range(2, number):
        if number% num ==0:
            break
    else:
         print(number)  

n = 10
a,b=0,1
for i in range(n):
    print(a, end=' ')
    a,b=b,a+b

n = 5
factorial=1
for i in range(1, n+1):
    factorial*=i
print(factorial)

from collections import Counter
list1 = [1, 1, 2]
list2 = [2, 3, 4]
counter1 = Counter(list1)
counter2 = Counter(list2)
diff1 = counter1 - counter2
diff2 = counter2 - counter1
result = list(diff1.elements()) + list(diff2.elements())
print(result)
