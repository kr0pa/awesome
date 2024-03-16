from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages
from .forms import ProfileModelForm
from .models import Profile, User

# Create your views here.
@login_required
def profile_view(request, username=None):
    if username:
        # profile = get_object_or_404(Profile, user__username = username)
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404()
    
    return render(request, 'a_users/profile.html', {'profile': profile})


@login_required
def profile_edit(request):
    form = ProfileModelForm(instance=request.user.profile)
    
    if request.method == 'POST':
        form = ProfileModelForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        
        if form.is_valid():
            form.save()
            return redirect('app_users:profile_view')
        
    if request.path == reverse('app_users:profile_onboarding'):
        template = 'a_users/profile_onboarding.html'
    else:
        template = 'a_users/profile_edit.html'
    
    return render(request, template, {'form': form})


@login_required
def profile_delete(request):
    user = request.user
    
    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, "Konto zostało usunięte!")
        return redirect('home')
    
    return render(request, 'a_users/profile_delete.html')