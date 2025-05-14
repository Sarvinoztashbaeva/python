try:
    a = int(input('Enetr any number: '))
    b = int(input('Enetr any number: '))
    print(a/b)
except ZeroDivisionError:
    print('ZeroDivisionError happend.')

try:
    user_input = int(input('Enter number:'))
    print(user_input)
except ValueError:
    print('your input is not integer. Plese write in integer form.')

try:
    with open('smth.txt','r') as file:
        print(file.read())
except FileNotFoundError:
    print('File not found')

try:
    a = 123
    b = 'anything'
    print(a+b)
except TypeError:
    print('TypeError happend')

import os
import stat
filename = 'example.txt'
with open(filename, 'w') as f:
    f.write('Sample content')
os.chmod(filename, stat.S_IREAD)
try:
    with open('example.txt', 'w') as z:
        z.write("smth new")
except PermissionError:
    print('PermissionError happend')

list1 = [12,333,'hello']
try:
    print(list1[3])
except IndexError:
    print('IndexError happend')

try:
    while True:
        user_input = input("Enter something (Ctrl+C to exit): ")
        print(f"You entered: {user_input}")
except KeyboardInterrupt:
    print("\nProgram terminated by user.")

try:
    a= 6
    b = 0
    print(a/b)
except ArithmeticError:
    print('ArthmeticError happend.')

bad_bytes = b'\xff\xfe\xfd'
try:
    text = bad_bytes.decode('utf-8')
except UnicodeDecodeError:
    print("UnicodeDecodeError happend")

list1 = [1,'hello',3]
try:
    list1.push(4)
except AttributeError:
    print('AttributeError happend')

with open('Note.txt', 'r') as f:
    print(f.read())

def read_first_n_lines(filename, n):    
    with open(filename, 'r') as f:
        lines = f.readlines()[:n]
        for line in lines:
            print(line.strip())

def append_to_file(filename, text_to_append):
    with open(filename, 'a') as file:
        file.write(text_to_append + '\n')
        with open(filename, 'r') as file:
        print("Updated file content:")
        print(file.read())
append_to_file("newfile.txt", "First line in a new file")

def read_last_n_lines(filename, n):
    with open(filename,'r') as file:
        lines = file.readlines()
        last_lines = lines[-n:]
        for line in last_lines:
            print(line.strip())

with open('example.txt', 'r') as file:
    lines = [line.strip() for line in file]
    print(lines)

----------------







