def caching_fibonacci():
    
    cash = {}
    def fibonacci(n:int)->int:        
        if n <=0: return 0
        if n == 1: return 1
        if n in cash: return cash[n]

        cash[n]=fibonacci(n-1)+ fibonacci(n-2)

        return cash[n]        
    
    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))