num = int(raw_input("Enter a number:"))
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print "Factorial of %d is %d." % (num, fact(num))
