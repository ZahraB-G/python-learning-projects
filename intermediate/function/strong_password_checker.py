def is_strong(password):
    if len(password) < 8:
        return False, "The Length of password should be 8 characters or more."
    elif str.islower(password) == False:
        return False, "Password must have at least one lower case charactor."
    elif str.isupper(password) == False:
        return False, "Password must have at least one upper case charactor."
    elif str.isdigit(password) == False:
        return False, "Password must contains at least one digit."
    else:
        return True, "Password is strong!"

print(is_strong('password'))