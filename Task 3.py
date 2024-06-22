def check_password_strength(password):
    """
    Checks the strength of a password based on specified criteria.
    
    Args:
        password (str): The password to assess.
    
    Returns:
        str: A message indicating the strength level.
    """
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(char in "!@#$%^&*()_+-=[]{}|;:'\",.<>?/" for char in password)

    # Assess strength based on criteria
    if length >= 8 and has_uppercase and has_lowercase and has_digit and has_special_char:
        return "Strong password! 🚀"
    elif length >= 6 and (has_uppercase or has_lowercase) and has_digit:
        return "Moderate password. Consider adding special characters."
    else:
        return "Weak password. Aim for longer length and more complexity."

# Example usage
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    strength_message = check_password_strength(user_password)
    print(strength_message)
