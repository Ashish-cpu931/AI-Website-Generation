# Email Validation

def validate_email(email):
    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if not username or not domain:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True

email = input("Enter an email address: ")

if validate_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")