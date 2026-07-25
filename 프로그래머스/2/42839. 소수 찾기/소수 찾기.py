from itertools import permutations

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    all_num = set()
    
    for length in range(1, len(numbers)+1):
        for j in permutations(numbers, length):
            num = int(''.join(j))
            all_num.add(num)
    
    count = 0 
    for i in all_num:
        if isPrime(i):
            
            count+=1
            
    return count