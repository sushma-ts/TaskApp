from django.urls import path, reverse_lazy
import pandas as pd
from . import views
from django.contrib.auth.views import (
    LogoutView
)

app_name = 'usercredentials'

urlpatterns = [


    path('signin/', views.SignInView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(template_name='usercredentials/logout.html'), name='logout'),
    path('Success/', views.SuccessView.as_view(), name='Success'),
   

]

