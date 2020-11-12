from django import forms
from django.core import validators
from CustApp.models import WorkOrder


class workForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ('TypeRepair',)

class customerForm(forms.Form):

    first_Name=forms.CharField(min_length=1, max_length=30, strip=True,
        widget=forms.TextInput(attrs={'placeholder':'First name', 'style':'font-size:small'}),
        validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(30)]
        )

    last_Name=forms.CharField(min_length=1,max_length=30, strip=True,
        widget=forms.TextInput(attrs={'placeholder':'Last name','style':'font-size:small'}),
        validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(30)]
        )

    phone_Number=forms.CharField(min_length=1, max_length=30, strip=True,
        widget=forms.TextInput(attrs={'placeholder':'Phone number','style':'font-size:small'}),
        validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(30)]
        )

    address=forms.CharField( strip=True, max_length=30,
        widget=forms.TextInput(attrs={'placeholder':'Customers address (not needed)','style':'font-size:small'}),
        validators=[ validators.MaxLengthValidator(30)]
        )


class deviceForm(forms.Form):

    Device_Name=forms.CharField(min_length=1, max_length=30, strip=True,
        widget=forms.TextInput(attrs={'placeholder':'Device Name', 'style':'font-size:small'}),
        validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(30)]
        )

    Color=forms.CharField(min_length=1,max_length=30, strip=True,
        widget=forms.TextInput(attrs={'placeholder':'Color of the Device','style':'font-size:small'}),
        validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(30)]
        )

    Device_type=forms.CharField(min_length=1, max_length=30, strip=True,
        widget=forms.TextInput(attrs={'placeholder':'Device type, Eg: computer/phone/tablet','style':'font-size:small'}),
        validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(30)]
        )

    Model_Number=forms.CharField(min_length=1, strip=True, max_length=30,
        widget=forms.TextInput(attrs={'placeholder':'Model_Number','style':'font-size:small'}),
        validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(30)]
        )

    Manufacture=forms.CharField(min_length=1, strip=True, max_length=30,
        widget=forms.TextInput(attrs={'placeholder':'Manufacture','style':'font-size:small'}),
        validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(30)]
        )
