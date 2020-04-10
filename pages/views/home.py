from django.shortcuts import render
from django.contrib.auth.models import User

def home_view(request):
    user = User.objects.all().count()
    context =  {
        'title': 'Home Page',
        'users': user
    }
    return render(request, 'pages/home.html', context)