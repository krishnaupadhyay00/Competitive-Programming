#WAP to accept a number from 1 to 7 and display the name of the day, like 1 for
Sunday, 2 for Monday, etc.


day_num = int(input("Enter a number (1-7): "))


if day_num == 1:
    print("Sunday")
elif day_num == 2:
    print("Monday")
elif day_num == 3:
    print("Tuesday")
elif day_num == 4:
    print("Wednesday")
elif day_num == 5:
    print("Thursday")
elif day_num == 6:
    print("Friday")
elif day_num == 7:
    print("Saturday")
else:
    print("Invalid Input! ")
