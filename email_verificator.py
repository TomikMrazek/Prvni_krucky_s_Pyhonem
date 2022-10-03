import re

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# Define a function for
# for validating an Email
def check(e_mail):
    # pass the regular expression
    # and the string into the fullmatch() method
    if re.fullmatch(regex, e_mail):
        print("Valid Email")

    else:
        print("Invalid Email")


# Driver Code
if __name__ == '__main__':
    # Enter the email
    print('Please, insert your e-mail address for valid:')
    email = input()

    # calling run function
    check(email)
