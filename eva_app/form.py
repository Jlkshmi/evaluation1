from django import forms

from eva_app.models import Employee


class WorkForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields=('name','age','email')