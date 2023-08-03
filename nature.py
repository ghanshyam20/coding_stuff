#**kwargs=this way the funtion will receive a dictionary of arguments,and can access the items accordingly.


def my_function(**surname):
    print("His last name is"+" " + surname["lname"] )


my_function(fname="naryan",lname="ghimire")


