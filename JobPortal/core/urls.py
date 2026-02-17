from django.urls import path
from .views import *
urlpatterns = [
  path('', home, name='home'),
  path('jobs/', jobs, name='jobs'),
  path('register/', register, name='register'),
  path('login/', login, name='login'),
  path('logout/', logout_view, name='logout'),
  path('job_details/<int:job_id>/', job_details, name='job_details'),
  path('contact/',  contact, name='contact'),
  path('profile/', profile, name='profile'),
  path('blog/', blog, name='blog'),
  path('blog_details/', blog_details, name='blog_details'),
  path('about/', about, name='about'),
  path('post_job/', post_job, name='post_job'),
]