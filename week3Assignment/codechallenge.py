#Modulo
def large_power(base, exponent):
    result = base ** exponent
    
    if result > 5000:
        return True
    else:
        return False


print(large_power(10, 3))  
print(large_power(10, 4)) 

#Divisibility
def divisible_by_ten(num):
    return num % 10 == 0


print(divisible_by_ten(40))
print(divisible_by_ten(49))
