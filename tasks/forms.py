
from django import forms
from django.forms import ModelForm, Textarea, TextInput
from .models import * 
from django.utils.translation import gettext_lazy as _

#crispy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit,Button, Row, Column,  Fieldset

#validation and cleanup
from django.utils.html import strip_tags

class TaskForm(ModelForm):
    class Meta:
        model = Task

        fields = ["title", "description", "status","user"]

        error_messages = {
            'title': {
                'max_length': _("Title is too long."),
            },
        }
    #Form element arragement using crispy
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_tag  = False
        
        self.helper.layout = Layout(
              Fieldset(' ',
                 Row(
                   Column('title'),
                   css_class=''
                ),

                Row(
                   Column('description'),
                   css_class=''
                ),
        
                Row(
                   Column('status'),
                   css_class=''
                ),
                Row(
                    Column('user'),
                    css_class=''
                ),
                Row(
                    Button('cancel', 'Cancel', css_class='btn btn-secondary m-2'),
                    Submit('submit', 'Submit', css_class='btn iia-btn-bg-primary m-2'),
                    css_class='float-right'
                )

              )
        ) #layout closing       
        
    # this function will be used for the validation        
    def clean(self):

        # data from the form is fetched using super function
        cleaned_data = super(TaskForm, self).clean()

        #clean html tags from text fields and validating length
        cleaned_data['title'] = strip_tags(cleaned_data.get('title'))
        if len(cleaned_data['title']) > 50:
            self._errors['title'] = self.error_class([
                'Maximum 50 characters are allowed for title field!'])
        
        cleaned_data['description'] = strip_tags(cleaned_data.get('description'))
        cleaned_data['status'] = strip_tags(cleaned_data.get('status'))

        return cleaned_data
			