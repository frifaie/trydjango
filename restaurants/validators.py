from django.core.exceptions import ValidationError

CATEGORIES = ['Padang', 'Jawa', 'Sunda', 'Menado']

def validate_category(value):
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError("{0} is not a valid category".format(value))