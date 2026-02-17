# Job Portal - Django Web Application

![GitHub license](https://img.shields.io/github/license/omartamer002/Job-Portal)
![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)
![Django Version](https://img.shields.io/badge/django-5.1-green.svg)

A high-performance, feature-rich **Job Portal** built with Django. This platform bridges the gap between top talent and leading employers, offering a seamless experience for job discovery, career management, and recruitment.

## 🚀 Key Features

### For Employees
- **Personalized Profile**: Manage your professional identity with a dedicated dashboard.
- **Job Discovery**: Advanced search and filtering by category, location, and job nature (Full-time, Remote, etc.).
- **CV Management**: Upload and showcase your curriculum vitae to potential employers.
- **Interactive Search**: Dynamic keyword search for rapid results.

### For Employers
- **Streamlined Job Posting**: Comprehensive form to post jobs with full company branding.
- **Talent Identification**: View applicant profiles and manage recruitment workflows.
- **Company Branding**: Create and manage detailed company profiles with logos and contact info.
- **Secure Access**: Role-based authentication ensuring data privacy and security.

## 🛠️ Tech Stack

- **Backend**: Python 3.13, Django 5.x
- **Frontend**: HTML5, CSS3, JavaScript (Slick, Owl Carousel, Nice Select)
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Deployment**: Git, GitHub

## 📂 Project Structure

```bash
JobPortal/
├── core/               # Main application logic (models, views, urls)
├── JobPortal/          # Project configurations (settings, wsgi)
├── media/              # User-uploaded files (CVs, profile pics, logos)
├── static/             # CSS, JS, and image assets
├── templates/          # Responsive HTML templates
└── manage.py           # Django management script
```

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/omartamer002/Job-Portal.git
   cd Job-Portal
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # MacOS/Linux
   # venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the server**:
   ```bash
   python manage.py runserver
   ```

---
*Created by [Omar Tamer](https://github.com/omartamer002) - Software Engineer*
