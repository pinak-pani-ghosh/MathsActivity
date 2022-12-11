# activity 3
# to genetate the fibonacci sequence using user inp

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
n=int(input("Enter a limit: "))

def recur_fibo(n):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
       return(recur_fibo(n-1) + recur_fibo(n-2))


# check if the number of terms is valid
if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(recur_fibo(i))
       
