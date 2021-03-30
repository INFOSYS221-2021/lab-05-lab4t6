def fibonacci(n): 
    if n <= 0:
        return "Value does not exist"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else: 
        return fibonacci(n-1) + fibonacci(n-2)  #formula to find the nth value 

print(fibonacci(10))
    
