#banking system using function 

#at first we have to create  for our bank account
#after that despoit
#withdraw amount
#check balance

accounts=[]

def account_creation(account_number,account_holder,initial_balance=0):
    account={
        'account_number':account_number,
        'account_holder':account_holder,
        'balance':initial_balance
    }
    accounts.append(account)


def deposit(account_number,amount):
    for account in accounts:
        if account['account_number']==account_number:
            account['balance']+=amount
            print(f"Deposit {amount}.New balance:{account['balance']}")
        else:
            print("Account not found.")



def withdraw(account_number,amount):
    for account in accounts:
        if account['account_number']==account_number:
            if amount<=account['balance']:
                account['balance']-=amount
                print(f"Withdraw {amount}.New balance:{account['balance']}")


            else:
                print("insufficient balance.withdraw cancelled")

def check_balnce(account_number):
    for account in accounts:
        if account['account_number']==account_number:
            print(f"Account holder:account{['account_holder']}")
            print(f"Account balance:{account['balance']}")



def main():
    while True:
        print("\n welcome to the simple banking system")
        print("1.create account")
        print("2.Deposit")
        print("3. Withdraw")
        print("4.Check Balance")
        print("5.Exit")

        choice=int(input("enter your choice"))

        if choice==1:
            account_number=int(input("enter account number:"))
            account_holder=str(input("enter your name:"))
            initial_balance=float(input("enter the inital balance"))
            account_creation(account_number,account_holder,initial_balance)

        elif choice==2:
            account_number=int(input("enter account number:"))
            amount=float(input("enter amount you want to deposit"))
            deposit(account_number,amount)

        elif choice==3:
               account_number=int(input("enter account number:"))
               amount=float(input("enter withdrawl amount"))
               withdraw(account_number,amount)

        elif choice==4:
            account_number=int(input("enter your account number"))
            check_balnce(account_number)

        elif choice==5:
            print("Thank you for using our system")
            break

        else:
            print("Invalid choice")

if __name__=='__main__':
    main()




        


   


    




            





