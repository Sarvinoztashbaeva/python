fruits = ['apple', 'banana', 'kivi', 'peach', 'grape']
print(fruits[2])

l1 = [2, 45, 9, 30]
l2 = ['hello', 27, 'BOB']
l1.extend(l2)
print(l1)

mylist = [2, 50, 38, 14, 4, 33, 49]
newlist = [mylist[0], mylist[len(mylist)//2], mylist[-1]]
print(newlist)

my_list = ['Twilight', 'You', 'Devil wears Prada', 'Internship', 'Avatar']
my_tuple = tuple(my_list)
type(my_tuple)

mylist = ['Tashkent', 'London', 'Tokyo']
print("Paris" in mylist)

list1 = [1, 9, 3, 8]
list2 = list1 * 2
print(list2)

l1 = [5, 20, 47, 98, 304]
l1[0], l1[-1]=l1[-1], l1[0]
print(l1)

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(my_tuple[3:7])

mylist = ['red', 'blue', 'grey', 'yellow', 'blue']
print(mylist.count('blue'))

mytuple = ('dog', 'hippo', 'lion', 'cat')
mytuple.index('lion')

my_tuple1 = (32, 345, 54, 21, 43)
my_tuple2 = (43, 7, 30, 52, 00)
new_tuple = my_tuple1 + my_tuple2
print(new_tuple)

newlist = ['i am', 'tired', 'to', 'create', 'new', 'lists']
newtuple = ('the', 'same', 'with', 'tuples')
print(len(newlist))
print(len(newtuple))

newtuple = ('the', 'same', 'with', 'tuples')
list1 = list(newtuple)
type(list1)

newtuple = (23, 55, 304, 1, 505, 46)
print(max(newtuple), min(newtuple))

tuple1 = ('my', 'last', 'tuple')
print(tuple1[::-1])


