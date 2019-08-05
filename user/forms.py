from django import forms

class LoginForm(forms.Form):
    collegeId = forms.CharField(label='College Id', max_length=100)
    password = forms.CharField(label='Password', max_length=100)

class RegisterForm(forms.Form):
    password = forms.CharField(required=True, label='Password', max_length=1000)
    email = forms.EmailField(required=True, label='Email', max_length=500)
    role = forms.CharField(required = True, label='Role', max_length=50)
    name = forms.CharField(required = True, label='Name', max_length=500)

class MarksForm(forms.Form):
    subject1 = forms.IntegerField(required=True, label='Subject 1')
    subject2 = forms.IntegerField(required=True, label='Subject 2')
    subject3 = forms.IntegerField(required=True, label='Subject 3')