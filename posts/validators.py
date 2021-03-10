from django import forms


def validator_not_empty(value):
    if value == '':
        raise forms.ValidationError(
            'Посты без текста мало людей заинтересует, '
            'пожалуйста, поделитесь своей историей!',
            params={'value': value},
        )
