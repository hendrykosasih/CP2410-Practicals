
a = int(input("Higher number? >>> "))
b = int(input("Lower number? >>> "))

if a%b == 0:
    print (("True! {1} is the factor of {0}.").format(a,b))
else:
    print((("Oops! {1} is not the factor of {0}.").format(a,b)))

