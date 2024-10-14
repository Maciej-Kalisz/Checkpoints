has_key = False
finished = False

print ("There are 2 boxes on the table.")

while not finished:
    print("There is a big box and a little box ")
    print("""\
Options:
[1] Open big box
[2] Open little box
        """)

    boxOptions = [1, 2]

    while True:
        try:
            boxChoice = int(input("Which would you like to pick? "))

            if not boxChoice in boxOptions:
                print("Invalid option. Please try again.")
            else:
                break

        except ValueError:
            print("Invalid option. Please try again.")

    match boxChoice:
        case 1:
            # Big box opened
            print("The big box contains a small locked box.")

            if has_key:
                print("Congratulations, you have found the golden token!")
                finished = True
            else:
                print("You need to find the key first.")

        case 2:
            print("The small box contains a key. You take the key. You'll need it later.")
            has_key = True

        case _:
            print("Invalid choice provided")