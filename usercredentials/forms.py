from django import forms
from django.forms import ModelForm, TextInput
#using register form and Django Authentication
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 

from django.utils.translation import gettext_lazy as _ #for custom labels
from django.contrib.auth.models import User
#crispy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit,Button, Row, Column,  Fieldset, HTML

#validation and cleanup
from django.utils.html import strip_tags

#login form with captcha
class LoginForm(AuthenticationForm):   
    widgets = {
          "username": TextInput(attrs={'autocomplete': 'off'  }),
          "password": TextInput(attrs={'autocomplete': 'off'  }),
    }

    #Form element arragement using crispy
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag  = False

        self.helper.layout = Layout(
              Fieldset('',
                 Row(
                   Column('username'),
                   css_class=''
                ),
                 Row(
                   Column('password'),
                   css_class=''
                ),              
             )
       )

    # this function will be used for the validation
    def clean(self):

        # data from the form is fetched using super function
        super(LoginForm, self).clean()

        # getting username and password from cleaned_data
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # validating the username and password
        if len(username) < 5:
            self._errors['username'] = self.error_class(['A minimum of 5 characters is required'])

        if len(password) < 8:
            self._errors['password'] = self.error_class(['Password length should not be less than 8 characters'])

        # return any errors if found
        return self.cleaned_data


