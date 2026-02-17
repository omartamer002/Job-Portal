from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Company(models.Model):
    company_logo = models.ImageField(upload_to='media/company_pics/')
    company_name = models.CharField(max_length=20, unique=True, null=False, blank=False)
    company_location = models.CharField(max_length=255, null=False, blank=False)
    company_email = models.EmailField(null=False, blank=False)
    company_website = models.URLField(null=False, blank=False)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

class Job(models.Model):
    JOB_CHOICES = (
        ('Software Engineering','Software Engineering'),
        ('IT', 'Information Technology'),
        ('Cybersecurity', 'Cybersecurity'),
        ('Data Analysis', 'Data Analysis'),
        ('Data Science', 'Data Science'),
        ('Machine Learning', 'Machine Learning'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('UI/UX Design', 'UI/UX Design'),
        ('Business Analysis', 'Business Analysis'),
        ('Quality Assurance', 'Quality Assurance'),
        ('DevOps', 'DevOps'),
        ('Cloud Computing', 'Cloud Computing'),
        ('Networking', 'Networking'),
        ('Database Administration', 'Database Administration'),
        ('Technical Support', 'Technical Support'),
    )
    JOB_NATURE_CHOICES = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Freelance', 'Freelance'),
        ('Hybrid', 'Hybrid'),
        ('Remotely', 'Remotely'),
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False, blank=False)
    job_choices = models.CharField(choices=JOB_CHOICES, max_length=100, null=False, blank=False)
    job_title = models.CharField(max_length=100, null=False, blank=False)
    vacancy = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], null=False, blank=False)
    salary_from = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)], null=False, blank=False)
    salary_to = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)], null=False, blank=False)
    job_experience = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)], null=False, blank=False)
    job_location = models.CharField(max_length=255, null=False, blank=False)
    job_details = models.TextField(null=False, blank=False)
    job_requirements = models.TextField(null=False, blank=False)
    job_expiry_date = models.DateTimeField(null=False, blank=False)
    job_nature = models.CharField(choices=JOB_NATURE_CHOICES, max_length=20, null=False, blank=False)
    
    def __str__(self):
        return self.job_title
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

class Contact(models.Model):
  message = models.TextField(null=False, blank=False)
  name = models.CharField(max_length=100, null=False, blank=False)
  email = models.EmailField(null=False, blank=False)
  subject = models.CharField(max_length=100, null=False, blank=False)
  
  def __str__(self):
    return f"Message from {self.name} about {self.subject}"

class Profile(models.Model):
    USER_TYPES = (
        ('employee', 'Employee'),
        ('employer', 'Employer'),
    )
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.user_type})"