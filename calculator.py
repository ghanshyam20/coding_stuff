def add(x,y):
    return x+y



def subtract(x,y):
    return x-y



def muliply(x,y):
    return x*y



def divide(x,y):
    if y!=0:
        return x/y
    

    else:
        return "goodbye you stupid we cannot divide by zero"
    


while True:
    print("Options:")
    print("1.ADD")
    print("2.Subtract")

    print("3.Multiply")

    print("4.Divide")

    print("5.Exit")


    choice=input("ENter your choice(1/2/3/4/5):")


    if choice=='5':
        print("you can go bruhh")
        break


    num1=float(input("Enter you first number"))

    num2=float(input("enter your second number"))



    if choice =='1':
        print("Result:",add(num1,num2))

    elif choice=='2':
        print("Result:",subtract(num1,num2))



    elif choice=='3':
        print("Result",muliply(num1,num2))

    elif choice=='4':
        print("Result",divide(num1,num2))


    else:
        print("Invalid choice")


    
    









 






