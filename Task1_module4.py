def factorial(var):
    var= int(var)
    if var < 2 :
        return 1
    else:
        return var * factorial(var-1)

var1 = input("Enter a number :")
#var1=int(var1)
fact = factorial (var1)

print("Factorial of ",var1, ' is :', fact)