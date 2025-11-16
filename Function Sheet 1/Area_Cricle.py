#  You are given a positive integer A denoting the radius of a circle. You have to calculate the area
#  of the circle.

def area_of_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    return area
A = 7   
print("Area of the circle is:", area_of_circle(A))