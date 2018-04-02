from django import forms

from .models import Item
from patients.models import PatientsInfo

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'user',
            'patient',
            'name',
            'age',
            'gender',
            'ethnicity',
            'smoker',
            'initial_visit',
            'fever',
            'public'
        ]

    def __init__(self, user=None, *args, **kwargs):
        print(user)
        print(kwargs)
        super(ItemForm, self).__init__(*args,**kwargs)
        self.fields['patient'].queryset = PatientsInfo.objects.filter(owner=user)