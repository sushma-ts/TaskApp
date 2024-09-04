from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

#auth
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.utils.http import url_has_allowed_host_and_scheme, urlsafe_base64_decode
from django.contrib import messages
from .import views
#For View types
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView

#forms
from .forms import LoginForm 
#for reset password form
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.tokens import default_token_generator

#Database
from django.contrib.auth.models import User
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model
from django.db import IntegrityError

from django.conf import settings
from django.template.loader import render_to_string

UserModel = get_user_model()

#Login page
class SignInView(FormView):
    form_class = LoginForm
    template_name = 'usercredentials/login.html'   

    def get(self, request) :            
        form = LoginForm()# AuthenticationForm()
        return render(request,  'usercredentials/login.html', {'form':form })

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        #auth
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            form = login(self.request, user)

            if 'next' in self.request.GET:
                nexturl = self.request.GET['next']
                return redirect(nexturl)
            else: 
                return redirect('tasks/add')
                
        else:
            form = LoginForm() #AuthenticationForm()
            messages.error(self.request,f'Invalid username or password')
            return render(self.request, 'usercredentials/login.html', {'form': form})
               
        
class SuccessView(generic.TemplateView):
         template_name= 'usercredentials/success.html'




