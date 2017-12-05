from django import forms
from django.contrib.auth.models import User
from .models import Student, Company


class UserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'u_id', 'branch', 'cgpa', 'live_kt', 'dead_kt', 'profile', 'passing_year']


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'c_id', 'location']


class EligiForm(forms.Form):
    choices = ((True, 'YES'), (False, 'NO'))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': "mdl-textfield__input", 'rows': '5'}))
    cgpa_reqd = forms.FloatField(max_value=10, min_value=0, widget=forms.TextInput(attrs={'class': "mdl-textfield__input"}))
    live_kt = forms.ChoiceField(choices=choices, widget=forms.RadioSelect())
    dead_kt = forms.ChoiceField(choices=choices, widget=forms.RadioSelect())
    starting_sal = forms.FloatField()
    tech_skills = forms.CharField(widget=forms.Textarea(attrs={'class': "mdl-textfield__input", 'rows': '5'}))

