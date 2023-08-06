import math
def rectangle_area(length,width):
    return length*width



def circle_area(radius):
    return math.pi*radius**2


def triangle_area(base,height):
    return 0.5*base*height



shape=input("enter the shape (rectangle/circle/triangle)").lower()


if shape=='rectangle':
    length=float(input("enter the length of rectangle"))
    width=float(input("enter the value of width"))
    area=rectangle_area(length,width)

    print(f"the area of rectangle is {area}")


elif shape=='circle':
    radius=float(input("enter the radius of circle"))

    area=circle_area(radius)
    print(f"the area of circle is {area}")

elif shape=='triangle':
    base=float(input("enter the value of base"))
    height=float(input("enter the value of height"))
    area=triangle_area(base,height)
    print(f"the area of triangle is {area} ")


else:
    print("invalid shape")