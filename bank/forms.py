from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

Genders=(
        ( 'a','Мужчина'),
        ('b','Женщина'),
        ('c','Трансформер '),
    )
class personalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genders'].widget.attrs.update({'class': 'form-select form-select-lg mb-3'})
        self.fields['idd'].widget.attrs.update({'class': 'form-select form-select-lg mb-3'})


    class Meta:
        model = personal_data1
        fields = ['idd', 'passport_series', 'passport_number','habitation', 'registration', 'genders','first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'passport_series': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'passport_number': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'habitation': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'registration': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
         }


class infoname(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name']

class CreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-lg'})
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            # 'password1': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),

            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            # 'password2': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),

        }

# Cvv
class cartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['card_number'].widget.attrs.update({'class': 'form-control form-control-lg',"placeholder":"номер карты "})
        self.fields['name'].widget.attrs.update({'class': 'form-select form-select-lg mb-3'})
        self.fields['term'].widget.attrs.update({'class': 'form-control form-control-lg' ,"placeholder": "MM/YYYY" })
        self.fields['Cvv'].widget.attrs.update({'class': 'form-control form-control-lg',"size":"1", "minlength":"3" ,"maxlength":"3" ,"placeholder": "cvv" })
    class Meta:
        model = card
        fields = ['card_number', "term", 'name','Cvv']


class cartForm2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['card_number'].widget.attrs.update({'class': 'form-control form-control-lg',"placeholder":"номер карты "})
        self.fields['name'].widget.attrs.update({'class': 'form-select form-select-lg mb-3'})
        self.fields['term'].widget.attrs.update({'class': 'form-control form-control-lg' ,"placeholder": "MM/YYYY" })
        self.fields['Cvv'].widget.attrs.update({'class': 'form-control form-control-lg',"size":"1", "minlength":"3" ,"maxlength":"3" ,"placeholder": "cvv" })
        self.fields['balance'].widget.attrs.update({'class': 'form-select form-control-lg  ',"placeholder":"пополнить счет "})
    class Meta:
        model = card
        fields = ['card_number', "term", 'name','Cvv','balance']

class homeForm(forms.ModelForm):
    class Meta:
        model=homes
        fields=['complex','description', "link", "metro",'photo']

class housingForm(forms.ModelForm):
    class Meta:
        model=housing_cost
        fields='__all__'
class login_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'form-control form-control-lg'})

        self.fields['percent'].widget.attrs.update({'class': 'form-control form-control-lg' ,"value":"7" , "min":"5" ,"max":"15"})
        self.fields['loan'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['term'].widget.attrs.update({'class': 'form-control form-control-lg' ,"max":"30"})

    class Meta:
        model=credit
        fields=['login','percent', "loan", "term"]

class information_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['salary'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['login'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['relationship'].widget.attrs.update({'class': 'form-select form-select-lg mb-3'})
        self.fields['children'].widget.attrs.update({'class': 'form-select form-select-lg mb-3'})
    class Meta:
        model = information
        fields = '__all__'

class creditw(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['loan'].widget.attrs.update({'class': 'form-range',"min":"0" ,"max":"5", "step":"0.5", 'id':"customRange3"})
    class Meta:
        model=credit
        fields='__all__'

class estateform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['login'].widget.attrs.update({'class': 'form-control form-control'})

    class Meta:
        model=estate
        fields='__all__'