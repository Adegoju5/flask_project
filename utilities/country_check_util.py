import pycountry

def is_valid_country(country_name):
    try:
        country = pycountry.countries.lookup(country_name)
        return True
    except LookupError:
        return False