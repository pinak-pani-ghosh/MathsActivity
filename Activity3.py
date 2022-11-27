a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
n=int(input("Enter a limit: "))
print(a)
print(b)
x=1
for x in range(3, n+1):
        if x<=n:
            a,b=b,a+b
            print(b)
            x=+1
