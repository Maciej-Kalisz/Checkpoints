has_key = False
finished = False

print ("There is a Russian doll on the table. You open it and find two more dolls, one blue one green.")

while not finished:
    print("There is a green Russian doll and a blue Russian doll on the table.")
    print("""\
Options:
[1] Open blue doll
[2] Open green doll
        """)

    blueGreenOptions = [1, 2]

    while True:
        try:
            blueGreenChoice = int(input("Which would you like to pick? "))

            if not blueGreenChoice in blueGreenOptions:
                print("Invalid option. Please try again.")
            else:
                break

        except ValueError:
            print("Invalid option. Please try again.")

    match blueGreenChoice:
        case 1:
            # Blue doll opened
            print("The doll contains a small locked box.")

            if has_key:
                print("Congratulations, you have found the golden token!")
                finished = True

        case 2:
            print("The doll contains a small key. You take the key.")
            has_key = True

        case _:
            print("Invalid choice provided")