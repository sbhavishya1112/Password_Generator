import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    """Load contacts from file, return empty dict if file doesn't exist."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_contacts(contacts):
    """Save contacts dictionary to file."""
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Name: ").strip()
    if name in contacts:
        print("A contact with this name already exists.")
        return

    phone = input("Phone number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")


def view_contacts(contacts):
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts saved yet.")
        return

    for name, details in contacts.items():
        print(f"{name} - {details['phone']}")


def search_contact(contacts):
    print("\n--- Search Contact ---")
    query = input("Enter name or phone number to search: ").strip().lower()
    results = {
        name: details for name, details in contacts.items()
        if query in name.lower() or query in details['phone']
    }

    if not results:
        print("No matching contacts found.")
        return

    for name, details in results.items():
        print(f"\nName: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")


def update_contact(contacts):
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    print("Leave a field blank to keep it unchanged.")
    phone = input(f"New phone [{contacts[name]['phone']}]: ").strip()
    email = input(f"New email [{contacts[name]['email']}]: ").strip()
    address = input(f"New address [{contacts[name]['address']}]: ").strip()

    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address

    save_contacts(contacts)
    print(f"Contact '{name}' updated successfully.")


def delete_contact(contacts):
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
    if confirm == 'y':
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Deletion cancelled.")


def print_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def main():
    contacts = load_contacts()

    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()