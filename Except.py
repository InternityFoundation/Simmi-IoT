try:
    a=int(input("enter any num:"))
    if a < 4:
        b = a / (a - 3)
    print("Value of b = ", b)
except(ZeroDivisionError, NameError):
    print("\nError Occurred and Handled")
