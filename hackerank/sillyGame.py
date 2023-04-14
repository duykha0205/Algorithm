
def is_prime(number):
    if number < 2:
        return False
    sieve = [True] * (number + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(number ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, number + 1, i):
                sieve[j] = False
    return sieve[number]

def remove_multiples(i, set_num):
    
    a = []
    
    for x in set_num:
        if x % i == 0:
            a.append(x)
            
    for y in a:
        set_num.remove(y)
            
    return

def check_set(set_num):
    
    for i in set_num:
        if is_prime(i):
            set_num.remove(i)
            remove_multiples(i, set_num)
            return 1

    return 0

def sillyGame_sol_01(n):
    # Write your code here
    set_num ={ _+1 for _ in range(n)}
    # print(set_num)
    
    flag = 0 #Alice
    
    while check_set(set_num):
        if flag:
            flag = 0
        else:
            flag = 1
    
    
    return "Alice" if flag else "Bob"


def sillyGame_Sol_02(n):
    # Write your code here
    set_num ={ _+1 for _ in range(n)}
    count = 0
    
    for i in set_num:
        if is_prime(i):
            count += 1
    
    
    return "Alice" if count%2!=0 else "Bob"

def primes(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
                
    count = 0
    primes_list = []
    for i in range(2, n+1):
        if sieve[i]:
            count += 1
    
    return count

def sillyGame_sol_03(n):
    primes_list = primes(n)
    print(primes_list)
    count = 0
    for i in range(len(primes_list)):
        if primes_list[i] > n:
            break
        count += 1
    return "Alice" if count % 2 == 1 else "Bob"

def isP(n):
    if n<=3:
        return True
    if ((n%2==0)|(n%3==0)):
        return False
    for d in range(5,int(n**.5)+1,6):
        if ((n%d==0)|(n%(d+2)==0)):
            return False
    return True

def getP(m):
    if m != 1:
        P=[2]
    else:
        return []
    
    for n in range(3,m+1,2):
        if isP(n):
            P.append(n)
    return P 
## final
def isPrime(x):
    for i in range(2, int(x ** .5) + 1):
        if not x % i: return False
    return True
    

def sillyGame(n):
    biggest_prime = primes[-1]
    if n > biggest_prime:
        for i in range(biggest_prime + 1, n + 1):
            if isPrime(i): primes.append(i)
    return 'Alice' if sum(i <= n for i in primes) % 2 else 'Bob'



print(sillyGame(1))