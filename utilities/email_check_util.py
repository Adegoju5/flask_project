from validate_email_address import validate_email

def is_functional_email(email):
    return validate_email(email, verify=True)