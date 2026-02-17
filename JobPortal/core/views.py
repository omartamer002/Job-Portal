from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator
from forms import JobForm, CompanyForm, ContactForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout 

def home(request):
  jobs = Job.objects.all()
  q = request.GET.get('q')
  location = request.GET.get('location')
  if q:
    jobs = jobs.filter(job_title__icontains=q)
  if location:
    jobs = jobs.filter(job_location__icontains=location)
  
  context = {
    'page_title': 'Home',
    'jobs': jobs[:5], # Slice at the end
    'locations': Job.objects.values_list('job_location', flat=True).distinct()
  }
  return render(request, 'core/home.html', context)

def jobs(request):
  jobs = Job.objects.all()
  q = request.GET.get('q') # Support keyword search from home page
  if q:
    jobs = jobs.filter(job_title__icontains=q)
  sort = request.GET.get('sort', '')
  if sort:
    if sort == 'salary_from':
      jobs = jobs.order_by('salary_from')
    elif sort == 'salary_to':
      jobs = jobs.order_by('-salary_to')
    elif sort == 'job_experience':
      jobs = jobs.order_by('-job_experience')
    elif sort == 'job_expiry_date':
      jobs = jobs.order_by('-job_expiry_date')
  category = request.GET.get('category', '')
  if category:
    jobs = jobs.filter(job_choices=category)
  nature = request.GET.get('nature', '')
  if nature:
    jobs = jobs.filter(job_nature=nature)
  location = request.GET.get('location', '')
  if location:
    jobs = jobs.filter(job_location__icontains=location)
  job_locations = Job.objects.values_list('job_location', flat=True).distinct()
  job_experiences = Job.objects.values_list('job_experience', flat=True).distinct()
  paginator = Paginator(jobs, 10)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  context = {
    'page_title': 'Jobs',
    'jobs': page_obj,
    'job_choices': Job.JOB_CHOICES,
    'job_nature': Job.JOB_NATURE_CHOICES,
    'job_locations': job_locations,
    'job_experiences': job_experiences,
  }
  return render(request, 'core/jobs.html', context)

def register(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if user_type == 'employee':
            username = request.POST.get('username')
            email = request.POST.get('email')
            full_name = request.POST.get('full_name')
            job_title = request.POST.get('job_title')
            profile_picture = request.FILES.get('profile_picture')
            cv = request.FILES.get('cv')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')

            user = User.objects.create_user(username=username, email=email, password=password)
            Profile.objects.create(
                user=user,
                user_type='employee',
                full_name=full_name,
                job_title=job_title,
                profile_picture=profile_picture,
                cv=cv
            )
            messages.success(request, 'Registration successful as Employee!')
            return redirect('login')

        elif user_type == 'employer':
            company_name = request.POST.get('company_name')
            company_email = request.POST.get('company_email')
            company_website = request.POST.get('company_website')
            
            # Using company_email or username as username for now as it's required
            username = company_email 
            if User.objects.filter(username=username).exists():
                messages.error(request, 'An account with this email already exists.')
                return redirect('register')

            user = User.objects.create_user(username=username, email=company_email, password=password)
            Profile.objects.create(
                user=user,
                user_type='employer',
                company_name=company_name,
                company_email=company_email,
                company_website=company_website
            )
            messages.success(request, 'Registration successful as Employer!')
            return redirect('login')

    context = {
        'page_title': 'Register'
    }
    return render(request, 'core/register.html', context)

@login_required(login_url='login')
def profile(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    context = {
        'page_title': 'Profile',
        'profile': user_profile
    }
    return render(request, 'core/profile.html', context)

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        login_form = LoginForm()
    context = {
        'page_title': 'Login',
        'login_form': login_form
    }
    return render(request, 'core/login.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')
    
def job_details(request, job_id):
  job = get_object_or_404(Job, id=job_id)
  context = {
    'page_title': 'Job Details',
    'job': job
  }
  return render(request, 'core/job_details.html', context)

def contact(request):
  if request.method == 'POST':
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
      contact_form.save()
      messages.success(request, 'Message sent successfully!')
      return redirect('contact')
    else:
      messages.error(request, 'Please correct the errors below.')
  else:
    contact_form = ContactForm()
  context = {
    'page_title': 'Contact',
    'contact_form': contact_form
  }
  return render(request, 'core/contact.html', context)

def blog(request):
  context = {
    'page_title': 'Blog'
  }
  return render(request, 'core/blog.html', context)

def blog_details(request):
  context = {
    'page_title': 'Blog Details'
  }
  return render(request, 'core/blog_details.html', context)

def about(request):
  context = {
    'page_title': 'About'
  }
  return render(request, 'core/about.html', context)

def post_job(request):
  if request.method == 'POST':
    company_form = CompanyForm(request.POST, request.FILES)
    job_form = JobForm(request.POST)
    
    if company_form.is_valid() and job_form.is_valid():
      company_name = company_form.cleaned_data.get('company_name')
      company, created = Company.objects.get_or_create(
          company_name=company_name,
          defaults=company_form.cleaned_data
      )
      
      job = job_form.save(commit=False)
      job.company = company
      job.save()
      
      messages.success(request, f'Job Listing for "{job.job_title}" has been posted successfully!')
      return redirect('home')
    else:
      messages.error(request, 'Please correct the errors below.')
  else:
    company_form = CompanyForm()
    job_form = JobForm()
    
  context = {
    'page_title': 'Post a Job',
    'company_form': company_form,
    'job_form': job_form
  }
  return render(request, 'core/post_job.html', context)
