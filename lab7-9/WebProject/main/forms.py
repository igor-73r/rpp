from .models import Total
from django.forms import ModelForm

class TotalForm(ModelForm):
    class Meta:
        model = Total
        fields = ['position', 'precipitation', 'date']
