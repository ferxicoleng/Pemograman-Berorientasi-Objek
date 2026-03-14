print("Enter guest names (type 'q' to quit):")

with open("guest_book.txt", "a") as file:

    while True:
        name = input("Enter name: ")

        if name.lower() == 'q':
            break

        file.write(name + "\n")
        print(f"Hello {name}, you have been added to the guest book.")