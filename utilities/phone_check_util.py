import phonenumbers
from phonenumbers import NumberParseException

def is_valid_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        return phonenumbers.is_valid_number(parsed_number)
    except NumberParseException:
        return False