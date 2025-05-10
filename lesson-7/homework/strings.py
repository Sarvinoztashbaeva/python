def is_prime(n):
    if n%2==0:
        return False
    elif n%2!=0:
        return True

def digit_sum(k):
    return sum(int(digit) for digit in str(abs(k)))

def power_2(n):
    k = 0
    while 2**k<=n:
        print(2**k)
        k+=1
