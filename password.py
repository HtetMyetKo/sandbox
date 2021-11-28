"""
Check login credentials

Password checker. Created by Cyrus. 25-11-2021
"""

def main():
    """Start program"""
    password = input("Enter password")
    if check_password(password):
        print("Logged in")
    else:
        print("Illegal access")


def check_password(password):
    return password == "12345"

main()