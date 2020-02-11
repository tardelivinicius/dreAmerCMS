from django.urls import path
from register.views import  Register
app_name = 'register'

urlpatterns = [
    path('', Register.step1, name='step1'),
    path('step2/', Register.step2, name='step2'),
    path('step3/', Register.step3, name='step3'),
]
