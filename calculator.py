import math

try:
    a = eval(input("Enter the first number: "))
    e = a
    while True:
        c = input(
            "what you want \n addition(+) \n subtract(-) \n multiplication(*) \n divide(/) \n(=) \npower(**) \n   :  ")

        if c == "=":
            print(e)
            break

        elif c == "+":
            b = eval(input("enter the2nd number :"))
            e += b
            print(e)
        elif c == "-":
            b = eval(input("enter the2nd number :"))
            e -= b
            print(e)
        elif c == "*":
            b = eval(input("enter the2nd number :"))
            e *= b
            print(e)
        elif c == "**":
            print(e*a)
            continue
        elif c == "/":
            b = eval(input("enter the2nd number :"))
            if b == 0 :
                print("invalid")
                exit()
            else:
                e /= b
                print(e)
        elif c not in ["+","-","*","/"]:
            print("invalid")
            exit()
        else :
            print(e)
            break
except (NameError, SyntaxError):
    print("Invalid data type. Please enter a valid number.")

