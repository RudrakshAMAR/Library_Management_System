def login(role):
    print(f"Logging in as {role}")
    return input("Enter your name: ")

def get_role():
    role = input("Are you a Librarian or a Member? (L/M): ").strip().upper()
    return "Librarian" if role == "L" else "Member"
