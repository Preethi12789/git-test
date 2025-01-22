import argparse
import json
import os


def load_data(json_file):
    """Load and return data from a JSON file, or return an empty list if file not found."""
    if not os.path.exists(json_file):
        return []
    with open(json_file, 'r') as f:
        return json.load(f)


def save_data(json_file, data):
    """Save data to a JSON file."""
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)


def list_users(data):
    """Print out the list of users."""
    if not data:
        print("No users found.")
        return
    print("List of users:")
    for user in data:
        print(f"- {user['name']} (Age: {user['age']}, Email: {user['email']})")


def add_user(data, name, age, email):
    """Add a new user to the data list."""
    # Validate that the user doesn't already exist by name
    for user in data:
        if user["name"].lower() == name.lower():
            print(f"User '{name}' already exists.")
            return

    new_user = {
        "name": name,
        "age": int(age),
        "email": email
    }
    data.append(new_user)
    print(f"Added user: {name}")


def update_user_age(data, name, new_age):
    """Update the age of a user identified by name."""
    for user in data:
        if user["name"].lower() == name.lower():
            user["age"] = int(new_age)
            print(f"Updated {name}'s age to {new_age}")
            return
    print(f"User '{name}' not found in the data.")


def main():
    # 1) Set up argument parser
    parser = argparse.ArgumentParser(
        description="A simple CLI tool to manage users in a JSON file."
    )

    # 2) Define possible actions
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all users."
    )
    parser.add_argument(
        "--add",
        nargs=3,  # we expect 3 arguments: name, age, email
        metavar=("NAME", "AGE", "EMAIL"),
        help="Add a new user with the given name, age, and email."
    )
    parser.add_argument(
        "--update",
        nargs=2,  # we expect 2 arguments: name, new_age
        metavar=("NAME", "NEW_AGE"),
        help="Update an existing user's age."
    )

    # 3) Parse the arguments
    args = parser.parse_args()

    # 4) Load existing data
    json_file = "data.json"
    data = load_data(json_file)

    # 5) Act based on arguments
    if args.list:
        list_users(data)
    elif args.add:
        name, age, email = args.add
        add_user(data, name, age, email)
        save_data(json_file, data)  # save after adding
    elif args.update:
        name, new_age = args.update
        update_user_age(data, name, new_age)
        save_data(json_file, data)  # save after updating
    else:
        # If no arguments provided, show help
        parser.print_help()


if __name__ == "__main__":
    main()
