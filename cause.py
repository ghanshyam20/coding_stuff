# using function calulate the area and perimeter of rectangle
#calculate the area of rectangle and perimeter
def rectangle_area(length,breath):
    return length*breath


def rectangle_perimeter(length,breath):
    return 2*(length + breath)



if __name__=="__main__":
    l=float(input("enter the length of rectangle"))
    b=float(input("enter the length of breath"))


    
print("area:",rectangle_area(l,b))
print("perimeter:",rectangle_perimeter(l,b))