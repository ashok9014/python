Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fibonacci_series(n):
   
    a, b = 0, 1
    series = []
    
    
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    
    return series


num_terms = 10
fib_series = fibonacci_series(num_terms)
print(f"The first {num_terms} terms of the Fibonacci series are: {fib_series}")