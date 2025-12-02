file_path = "inscribed.txt"
name = "Andrew"

    


# name = input("Who is Signing in: ")
# file_path = input('Where shall i save it: ') 


if name:
    with open("inscribed.txt", "w") as fp:
        fp.write("")
    
else:
    print("NO ACCESS!!")


