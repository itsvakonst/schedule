from django.shortcuts import redirect, render

from django.contrib.auth import login

from myproject.accounts.utils import send_telegram_message
from .models import User, Organization
from .forms import RegisterForm


from django.utils import timezone
from .models import Attendance
from django.contrib.auth.decorators import login_required

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


@login_required
def check_in(request):
    Attendance.objects.create(user=request.user, check_in=timezone.now())
    if request.user.telegram_id:
        send_telegram_message(request.user.telegram_id, 'Вы отметили приход.')
    return redirect('profile')

@login_required
def check_out(request):
    attendance = Attendance.objects.filter(user=request.user, date=timezone.now().date()).last()
    if attendance and not attendance.check_out:
        attendance.check_out = timezone.now()
        attendance.save()
    return redirect('profile')