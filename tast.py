
#make simple banking system account creation,money deposit ,withdraw,intrest and many more ahilesamman padhako kura sab include garera program gara ???


bank_name=str(input("enter the bank you want to join.."))

account_creation=str(input("enter your name ?"))
P=float(input("enter the amount you want to desposit.."))

T=float(input("enter the years you want to despot the money"))
R=float(input("enter the intrest rate you want.."))

intrest=(P*T*R)/100

my_withdraw="i want to join in the {}.My bank info is {}.At 2012 AD i created my account with the principal {} with the intrest rate {}% at the time of {} .I got intrest {}."

print(my_withdraw.format(bank_name,account_creation,P,T,R,intrest))
















