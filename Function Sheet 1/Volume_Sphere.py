#  You are given a positive integer A denoting the radius of a sphere. You have to calculate the
#  volume of the sphere.
#  Volume of a sphere having radius R is given by (4 * π * R3) / 3

def volume_of_sphere(radius):
    pi = 3.14159
    volume = (4/3) * pi * radius ** 3
    return volume
A = 5
print( volume_of_sphere(A))