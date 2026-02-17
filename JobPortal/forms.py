from django import forms
from core.models import Job, Company, Contact

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'company_location', 'company_email', 'company_website', 'company_logo']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your company name'}),
            'company_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City, Country'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'contact@company.com'}),
            'company_website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com'}),
            'company_logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_title', 'job_choices', 'vacancy', 'job_nature', 'job_experience', 'salary_from', 'salary_to', 'job_location', 'job_details', 'job_requirements', 'job_expiry_date']
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the job title'}),
            'job_choices': forms.Select(attrs={'class': 'form-control'}),
            'vacancy': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of vacancies'}),
            'job_nature': forms.Select(attrs={'class': 'form-control'}),
            'job_experience': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Years of experience'}),
            'salary_from': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary from'}),
            'salary_to': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary to'}),
            'job_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job location'}),
            'job_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter job details'}),
            'job_requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter required skills/requirements'}),
            'job_expiry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter your message'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
