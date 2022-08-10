l = [1,2,4,576,6]


while True:
    i = int(input("Enter index: "))
    try:
        print(l[i])
    except Exception as e:
        print("\n\nException occured " + str(e) + "\n\n")

    else:
        print("successful list access\n\n")
        break

    finally:
        print("\n\n\nfinally BLOCK\n\n\n")