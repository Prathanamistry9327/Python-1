6. Write python program that swap two number with temp variable and
without temp variable.

Ans:
   # Swap with a Temp Var:

a=50
b=100

print("before swapping value:")
print("a=",a)
print("b=",b)

temp=a
a=b
b=temp

print("After Swapping Value:")
print("a=",a)
print("b=",b)

    # Swap Without a Temp Var:

a=10
b=20

print("before swapping value:")
print("a=",a)
print("b=",b)

a=a+b
b=a-b
a=a-b

print("After Swapping Value:")
print("a=",a)
print("b=",b)