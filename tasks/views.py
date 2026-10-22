from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.models import Profile


# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
