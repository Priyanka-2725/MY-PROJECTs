class Contact:
    def _init_(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

contacts = []

def add_contact(name, phone, email):
    new_contact = Contact(name, phone, email)
    contacts.append(new_contact)
    print("Contact added successfully.")

def view_contacts():
    if contacts:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
    else:
        print("Contact list is empty.")

def search_contact(name):
    for contact in contacts:
        if contact.name == name:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
            return
    print("Contact not found.")

def update_contact(name, phone, email):
    for contact in contacts:
        if contact.name == name:
            contact.phone = phone
            contact.email = email
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact(name):
    for contact in contacts:
        if contact.name == name:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

# Simple text-based user interface
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == "4":
        name = input("Enter name to update: ")
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        update_contact(name, phone, email)
    elif choice == "5":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "6":
        print("Exiting the Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
