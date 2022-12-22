first = input("Enter The Frist Number : ")
operand = input("Enter The Operator (+, -, /, %)")
secound = input("Enter The Secound Number : ")

first = int(first)
secound = int(secound)

if operand=="+":
    print(first + secound)

elif operand=="-":
    print(first - secound)

elif operand=="*":
    print(first * secound)

else:
    print("Invalid Operation")