#implementing recursive algorithm for factorial
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

no=int(input("enter no. to find factorial:"))
factorial=fact(no)
print("factorial of number is:",factorial)        