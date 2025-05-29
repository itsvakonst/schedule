from django.shortcuts import render

from django.contrib.auth import login
from .models import User, Organization
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            # Если у пользователя нет приглашения — создаём организацию
            if not user.organization:
                org = Organization.objects.create(name=f"{user.username}'s Org")
                user.organization = org
                user.is_admin = True
            
            user.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
