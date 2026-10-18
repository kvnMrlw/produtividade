from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Profile


# Create your views here.
@login_required
def tutorial(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        profile.viu_turorial = True
        profile.save()
        redirect("/tasks/dashboard/")
    return render(request, 'tutorial.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
