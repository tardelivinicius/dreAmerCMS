from django.conf.urls import url, include
from login.views import login
app_name = 'login'

urlpatterns = [
    url(r'^', login),
]
