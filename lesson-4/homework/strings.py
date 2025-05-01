students_gpa = {'John':3.5, 'Ava':3.7, 'Mark':4.3, 'Stive':3.4, 'Ella':4.5}
sorted_asc = dict(sorted(students_gpa.items(), key=lambda item: item[1]))
sorted_desc = dict(sorted(students_gpa.items(), key=lambda item: item[1], reverse= True))
print(sorted_asc, sorted_desc)

numbers = {0: 10, 1: 20}
numbers[2]=30
print(numbers)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic_all = {}
dic_all.update(dic1)
dic_all.update(dic2)
dic_all.update(dic3)
print(dic_all)

n = int(input('Enter any number: '))
dict_sqr = {}

for x in range(1, n+1):
    dict_sqr[x] = x*x
print(dict_sqr)

dict1 = {}
for x in range(1, 16):
    dict1[x] =x*x
print(dict1)

my_set = {'a', 'hello', 505, 'as'}
type(my_set)

my_set = {'a', 'hello', '505', 'as'}
for smth in my_set:
    print(smth)

my_set = {'i', 'do not', 'know', 'what', 'to'}
my_set.add('write')
print(my_set)
my_set.update(['smth', 'interesting'])
print(my_set)

my_set = {'i', 'do not', 'know', 'what', 'to'}
print(my_set.pop())

my_set = {'i', 'do not', 'know', 'what', 'to'}
spacific_item = 'smth'
if spacific_item in my_set:
    my_set.remove(spacific_item)
    print(f'{spacific_item} was removed')
else:
    print(f'{spacific_item} not found')

print(my_set)





