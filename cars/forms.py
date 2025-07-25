from django import forms

from cars.models import Car
from cars.widgets import NoClearableFileInput



class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'description', 'image']

class CarCreateForm(CarBaseForm):
    pass

class CarUpdateForm(CarBaseForm):
    class Meta(CarBaseForm.Meta):
        widgets = {
            'image': NoClearableFileInput(),
        }
