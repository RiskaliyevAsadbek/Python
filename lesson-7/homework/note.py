# 1. is_prime(n) funksiyasi
# is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.
def is_prime (n: int) -> int:
    if  n < 2 :
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False    
    else:
        return True
      
print(is_prime(4))
print(is_prime(7))

# 2. digit_sum(k) funksiyasi
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

def digit_sum (n : int) -> int:
    total = 0
    for i in str(n):
        total += int(i)
    return total    

print(digit_sum(24))
print(digit_sum(502))

# 3. Ikki sonning darajalari
# Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

# 1st option 
def my_function(n: int) -> int:
    start = 1
    x = 2
    while x ** start <= n:
        print(x ** start)
        start +=1
my_function(10) 

# 2nd option
def my_function (n: int) -> int:
    for i in range(1, n):
        if 2 ** i <= n:
            print( 2 ** i)
        else: 
            break

my_function(10)       

# 3rd option
def my_function(n: int) -> int:
    start = 1
    x = 2
    result = [] 
    while x ** start <= n:
        result.append(x ** start)
        start +=1
    return result    
print(my_function(10)) 

# 4th option
def my_function (n: int) -> int:
    result = []
    for i in range(1, n):
        if 2 ** i <= n:
            result.append( 2 ** i)
        else: 
            break
    return result
print(my_function(10))        


