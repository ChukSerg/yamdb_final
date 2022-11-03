from rest_framework.serializers import ValidationError


class RestrictedValueForFields:
    '''checking fields for restricted values'''
    message = 'Fields "{fields}" contains restricted values "{values}"'

    def __init__(self, fields, values, message=None):
        '''
        fields - fields to check.
        values - list or tuple of restricted values
        '''
        self.fields = fields
        self.values = values
        self.message = message or self.message

    def __call__(self, data):
        print(data)
        values = [
            value for key, value in data.items()
            if key in self.fields
            and value in self.values
        ]
        if values:
            raise ValidationError(
                self.message.format(fields=self.fields, values=values)
            )
