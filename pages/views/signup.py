from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)