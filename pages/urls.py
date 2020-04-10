from django.urls import path
from pages.views import home_view, signup_view

app_name = 'pages'

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
]