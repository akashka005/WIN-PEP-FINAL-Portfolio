from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Skill, Project, Achievement, Education, ContactMessage

def index(request):
    skills = Skill.objects.all()
    skills_by_category = {
        'Languages': skills.filter(category='Languages'),
        'AI_ML': skills.filter(category='AI/ML Stack'),
        'Web_Tools': skills.filter(category='Web & Tools'),
    }
    
    projects = Project.objects.all().order_by('order', '-id')
    achievements = Achievement.objects.all()
    education = Education.objects.all()
    
    context = {
        'skills_by_category': skills_by_category,
        'projects': projects,
        'achievements': achievements,
        'education': education,
    }
    
    return render(request, 'portfolio/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(request, f"Thank you, {name}! Your message has been sent.")
        return redirect('index')
    
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'portfolio/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'portfolio/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('index')

@login_required
@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    projects = Project.objects.all().order_by('order', '-id')
    messages_list = ContactMessage.objects.all().order_by('-created_at')
    context = {
        'projects': projects,
        'contact_messages': messages_list,
    }
    return render(request, 'portfolio/dashboard.html', context)