first_number = int(input("Please type in the first number: "))
another_number = int(input("Please type in another number: "))

if first_number > another_number:
    print("The greater number was: ", first_number)
elif another_number > first_number:
    print("The greater number was:", another_number)
else:
    print('They are equal!!!!')
