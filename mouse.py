#calculate the area of rectange and  perimeter

#using function calculate the area and perimeter of ractange

def rectangle_area(length,breath):
    return length*breath




def rectangle_perimeter(length,breath):
    return 2*(length+breath)


if __name__=="__main__":
    l=float(input("ENter the length of rectangle:"))
    b=float(input("enter the breath of rectangle:"))



    print("area:",rectangle_area(l,b))
    print("perimeter:",rectangle_perimeter(l,b))






