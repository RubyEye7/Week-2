def all_same():
    value1 = input("1st number: ")
    value2 = input("2nd number: ")
    value3 = input("3rd number: ")

    if value1 == value2 and value2 == value3:
        print("The values are equal")
        return True
    else:
        print("The values are not equal")
        return False

all_same()
