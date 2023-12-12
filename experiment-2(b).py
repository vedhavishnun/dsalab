def fibonacci_series(n):
    if n<=1:
        return n
    else:
        return (fibonacci_series(n-1)+fibonacci_series(n-2))
n=int(input("enter no. of terms:"))
print("fibonacci series:")
for i in range(n):
    print(fibonacci_series(i))    