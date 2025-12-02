import random
friends = ["Brayan", "Mathias", "daniela", "roy", "Jean"]
for friend in friends:
    print("Is my name too short or too long -"+ friend )
    if len(friend) > 5:
        print("Your name is too long")
    if len(friend) <5:
        print("your name is too short")