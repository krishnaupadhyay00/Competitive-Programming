# Given the lengths of semi-major axis A and semi-minor axis B of an ellipse, calculate the Area
#  of the Ellipse.
#  Area of ellipse having semi-major axis length a and semi-minor axis length b is given by π * a * b.

def area_of_ellipse(a, b):
    pi = 3.14159
    area = pi * a * b
    return area
A = 5
B = 3
print( area_of_ellipse(A, B))