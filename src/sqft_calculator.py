while True:
    try:
        rooms = int(input("\nHow many rooms total? "))
        break
    except:
        print("Only integers are accepted for total rooms.")

inches = 0
for i in range(rooms):
    length = 0
    while True:
        try:
            length = int(input("\nLength of room " + str(i+1) + " in inches? "))
            break
        except:
            print("Only integers are accepted for length of room " + str(i+1) + ".")

    width = 0
    while True:
        try:
            width = int(input("Width of room " + str(i+1) + " in inches? "))
            break
        except:
            print("Only integers are accepted for width of room " + str(i+1) + ".")

    room = length * width
    inches += room

feet = inches / 12
sqft = feet / 12
print("\nThe total interior SQFT is " + str(sqft) + ".")