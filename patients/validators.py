from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )

def validate_email(value):
    email = self.cleaned_data.get("email")
    if ".edu" in email:
        raise ValidationError("We do not accept edu emails")



GENDER = ['Male','Female']

def validate_gender(value):
    cat = value.capitalize()
    if not value in GENDER:
        raise ValidationError(f"{value} not a valid gender")