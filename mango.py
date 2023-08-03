#convert fahrenheit to celcius and vice versa:
#using python function


def celcius_to_fehrenheit(celcius):
    return (celcius*9/5)+32



def fahrenheit_to_celcius( fahrenheit):
    return (fahrenheit-32)*5/9



def temperature_convertor():
    print("1.celcius to fahernheit")
    print("2.Fahernheit to celcius")

     
    
   

    choice=input("enter your choice:")

    if choice=='1':
        c=float(input("enter temperature in celcius"))
        f= celcius_to_fehrenheit(c)
        print("Temperature in fahrenheit:",f)

    elif choice=='2':
        f=float(input("enter temperature in fahernheit:"))
        c=fahrenheit_to_celcius(f)

        print("temperature in celcius is:",c)


    else:
        print("Invalid choice")


if __name__=="__main__":
    temperature_convertor()




    



