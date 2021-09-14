def main():
    while True:
        name = input("Enter a name: ")
        phone = input("Enter a phone number for this person: ")
        email = input("Enter their email: ")

        with open("contacts.txt","a") as person:
            person.write(f"{name}, {phone}, {email}\n")  # this is formated this way because it is called a CSV (Comma separated value)

        asks = input("Would you like to enter another person's info (Y|N)? ").lower()
        if asks == "y" or asks == "":
            continue
        else:
            break

if __name__ == "__main__":
    main()
