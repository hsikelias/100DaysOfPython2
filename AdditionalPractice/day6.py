print("Welcome To Contact Saver! You can Add/Update/Remove contacts, Edit existing contacts and even viewing all the saved contacts!")

# contacts = {"name":"","email":"","phone":""}
# this wont work because everytime a new contact is added it overwrites instead of creating a new contact, best is to use a
# list of dictionaries, each contact is its own dictionary
contacts_list = []
repeat = "y"

while repeat == "y":
    try:
        operation = int(input(
            "1.Add New Contact\n"
            "2.Edit Saved Contact\n"
            "3.Remove Saved Contacts\n"
            "4.View All Saved Contacts\n"
            "What do you want to do, Select a number?: "
        ))

        if operation ==1:
            name = (input("Enter the name of your new contact: "))
            email = (input("Enter the email of your new contact: "))
            phone = (input("Enter the phone number of your new contact: "))
        
            new_contact = {"name": name, "email":email,"phone":phone}
            contacts_list.append(new_contact)
            print(f"Contact for {name} added successfully!")

        elif operation ==2:
            print("You choose edit/update your saved contacts")


        elif operation ==3:
            print("You choose to remove a saved contact")

        elif operation ==4:
            # print([contacts_list]) Here im printing a set of single contacts
            # dictionary, which will only show the last overwritten contact
            if contacts_list:
                print("\n---- Your Saved Contacts ----")
                for contact in contacts_list:
                    print(f"Name: {contact['name']}")
                    print(f"Email: {contact['email']}")
                    print(f"Phone: {contact['phone']}")
                    print("--------------------------")
            else:
                print("No saved contacts yet.")
        else: 
            print("You did NOT enter a valid input, please make sure your number is between 1-5")
    except ValueError:
        print("Invalid input. Please enter a number.")
    
    repeat = input("Do you want to continue?(y/n):").lower()
print("Thanks for using Contact Saver :D")