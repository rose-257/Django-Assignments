from django import forms
from .models import student



class StudentForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=student.Genderchoices,widget=forms.RadioSelect)
    class Meta:
        model =student
        
        fields = ('firstname','lastname','email','phone','password','confirmpassword','gender')
        
        widgets = {
            
            'firstname':forms.TextInput(attrs={'class':'form-control','placeholder':'Firstname'}),
            'lastname':forms.TextInput(attrs={'class':'form-control','placeholder':'Lastname'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Password'}),
            'confirmpassword':forms.TextInput(attrs={'class':'form-control','placeholder':'Confirm password'}),
        }