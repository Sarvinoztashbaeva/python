year = int(input('Enter any year: '))

if (year%4==0 and year%100!=0) or (year%400==0):
    print(f'{year} is leap year')
else:
    print(f'{year} is not leap year')



n = int(input('n: '))
if n%2!=0:
    print('Weird')
elif n%2==0 and 2<=n<=5:
    print('not weird')
elif n%2==0 and 6<=n<=20:
    print('Weird')
else:
    print('not werid')



a = int(input("Enter a: "))
b = int(input("Enter b: "))

start = a if a <= b else b
end = b if b >= a else a
if start % 2 != 0:
    start += 1
even_numbers = list(range(start, end + 1, 2)) if start <= end else []
print(even_numbers)



a = int(input("Enter a: "))
b = int(input("Enter b: "))

start = min(a, b)
end = max(a, b)
start += start % 2
even_numbers = list(range(start, end + 1, 2))
print(even_numbers)
