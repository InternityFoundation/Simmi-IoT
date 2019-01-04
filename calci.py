print("1.Add")
print("2.Sub")
print("3.Multiply")
print("4.Divide")
select = int(input("select 1/2/3/4"))
if (select>=1 and select<=4):
    print("Enter two numbers: ")
    num1 = int(input())
    num2 = int(input())
    if select == 1:
    	res = num1 + num2
    	print("Result = " , res)
    elif select == 2:
    	res = num1 - num2
    	print("Result = " , res)
    elif select == 3:
    	res = num1 * num2;
    	print("Result = ", res)
    else :
    	res = num1 / num2;
    	print("Result = ", res)
else:
    print("invalid input")