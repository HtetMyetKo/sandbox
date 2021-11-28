"""
Check login credentials

Password checker. Created by Cyrus. 25-11-2021
"""

def main():
    """Start program"""
    password = "12345"
    if password == "12345":
        print("Logged in")
    else:
        print("Illegal access")


def check_password(password):
    return password == "12345"

main()