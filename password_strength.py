def check_password(password):
    """Rate a password and explain which characteristics it meets."""
    score = 0
    reasons = []

    if len(password) >= 8:
        score += 1
        reasons.append("At least 8 characters long")
    else:
        reasons.append("Too short: use at least 8 characters")

    if any(char.islower() for char in password):
        score += 1
        reasons.append("Contains lowercase letters")
    else:
        reasons.append("Add lowercase letters")

    if any(char.isupper() for char in password):
        score += 1
        reasons.append("Contains uppercase letters")
    else:
        reasons.append("Add uppercase letters")

    if any(char.isdigit() for char in password):
        score += 1
        reasons.append("Contains numbers")
    else:
        reasons.append("Add numbers")

    if any(not char.isalnum() for char in password):
        score += 1
        reasons.append("Contains special characters")
    else:
        reasons.append("Consider adding a special character")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, reasons

def main():
    """Get a password and display its strength assessment."""
    password = input("Enter a password to check: ")

    strength, reasons = check_password(password)

    print("\nPassword Strength:", strength)
    
    for reason in reasons:
        print("-", reason)


if __name__ == "__main__":
    main()
