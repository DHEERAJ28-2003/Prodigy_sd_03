import os

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            for line in f:
                name, phone, email = line.strip().split('|')
                contacts.append({'name': name, 'phone': phone, 'email': email})
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        for contact in contacts:
            f.write(f"{contact['name']}|{contact['phone']}|{contact['email']}\n")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print("✅ Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
        return
    print("\n📇 Contact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")
    print()

def edit_contact(contacts):
    view_contacts(contacts)
    try:
        choice = int(input("Enter the number of the contact to edit: ")) - 1
        if 0 <= choice < len(contacts):
            contacts[choice]['name'] = input("Enter new name: ")
            contacts[choice]['phone'] = input("Enter new phone: ")
            contacts[choice]['email'] = input("Enter new email: ")
            save_contacts(contacts)
            print("✏️ Contact updated.")
        else:
            print("❌ Invalid selection.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        choice = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= choice < len(contacts):
            deleted = contacts.pop(choice)
            save_contacts(contacts)
            print(f"🗑️ Deleted contact: {deleted['name']}")
        else:
            print("❌ Invalid selection.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    contacts = load_contacts()
    while True:
        print("\n📞 Contact Management Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

# Launch the contact manager
main()
