'''Read three angles of triangles and determine their types(Right triangle, Obtuse
triangle, Acute triangle).'''


a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))


if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    if a == 90 or b == 90 or c == 90:
        print("Right Triangle")
    elif a > 90 or b > 90 or c > 90:
        print("Obtuse Triangle")
    else:
        print("Acute Triangle")
else:
    print("Invalid Triangle")
