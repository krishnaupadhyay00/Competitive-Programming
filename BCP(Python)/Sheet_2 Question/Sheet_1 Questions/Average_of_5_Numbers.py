# 3. Average of 5 Numbers

A = int(input("Enter number A: "))
B = int(input("Enter number B: "))
C = int(input("Enter number C: "))
D = int(input("Enter number D: "))
E = int(input("Enter number E: "))
if A >= 0 and B >= 0 and C >= 0 and D >= 0 and E >= 0:
    average = (A + B + C + D + E) / 5
    print("Average of the numbers is:", average)
else:

    print("Invalid input! Numbers should be positive.")
