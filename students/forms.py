from django import forms
from .models import Student, Party 

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'email']

class PartyForm(forms.ModelForm): 
    class Meta: 
        model = Party 
        fields = ['name', 'date']