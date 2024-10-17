from django import forms 
from .models import Student 


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = ['name', 'email', 'password']
        # adding classes
        widgets = {'name':forms.TextInput(attrs={'class':'myclass'}), 'password':forms.PasswordInput(render_value=True, attrs={'class':'mypass'})}
