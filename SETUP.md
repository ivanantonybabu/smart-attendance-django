# Smart Attendance Monitoring System — Complete Setup & Development Documentation

## 1. Project Information

| Item | Details |
|---|---|
| Project | Smart Attendance Monitoring System |
| Framework | Django |
| Language | Python |
| Database | SQLite |
| Frontend | HTML5, CSS3 |
| Development OS | Ubuntu Linux |
| IDE | Visual Studio Code |
| Version Control | Git |
| Repository Hosting | GitHub |
| Application Type | Single-page web application |

---

## 2. Project Overview

The **Smart Attendance Monitoring System** is a web-based attendance management application developed using the Django framework.

The purpose of the project is to provide a simple digital platform for managing student attendance. Instead of maintaining attendance manually, the system provides a centralized web interface where student and attendance information can be recorded and monitored.

The project follows Django's **Model-View-Template (MVT)** architecture and uses SQLite for local database storage.

The application is designed as a **single-page interface**, where the major attendance-related functions are presented through one dashboard.

---

## 3. Main Objectives

The objectives of the project are:

1. Learn the fundamentals of Django.
2. Understand Django project and application structure.
3. Implement Django URL routing.
4. Create Django views.
5. Create and use HTML templates.
6. Work with Django models and databases.
7. Implement attendance-related functionality.
8. Create a simple single-page dashboard.
9. Understand virtual environments and Python package management.
10. Use Git for version control.
11. Publish the project on GitHub.
12. Document the project so that it can be reproduced on another computer.

---

## 4. Technologies and Tools

- **Python** — backend programming
- **Django** — web application framework
- **SQLite** — local database
- **HTML5/CSS3** — user interface
- **Bootstrap** — optional responsive styling
- **Visual Studio Code** — development environment
- **Ubuntu Linux** — development operating system
- **Git** — version control
- **GitHub** — source-code hosting

---

## 5. System Architecture

The project follows Django's Model-View-Template architecture.

```text
                    USER
                     |
                     v
              Web Browser
                     |
                     v
              Django URL
                     |
                     v
                   VIEW
              /           \
             /             \
            v               v
       TEMPLATE           MODEL
            \              |
             \             v
              \       SQLite DB
               \           |
                \          |
                 v          v
                HTML Response
                     |
                     v
                   USER
```

---

# 6. Prerequisites

Before starting, make sure Ubuntu has:

- Python 3
- pip
- Python virtual environment support
- Git
- Visual Studio Code
- A GitHub account
- A web browser

Check Python:

```bash
python3 --version
```

Check pip:

```bash
pip3 --version
```

Check Git:

```bash
git --version
```

Check virtual environment support:

```bash
python3 -m venv --help
```

If required packages are missing:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git -y
```

---

# 7. Create the Project Directory

Open the Ubuntu terminal:

```bash
mkdir smart_attendance_project
cd smart_attendance_project
```

Check the current location:

```bash
pwd
```

Expected format:

```text
/home/YOUR_USERNAME/smart_attendance_project
```

---

# 8. Open the Project in VS Code

From the project directory:

```bash
code .
```

If the `code` command is unavailable, open VS Code manually and select:

```text
File → Open Folder → smart_attendance_project
```

---

# 9. Create a Python Virtual Environment

Create the virtual environment:

```bash
python3 -m venv venv
```

This creates:

```text
smart_attendance_project/
└── venv/
```

---

# 10. Activate the Virtual Environment

On Ubuntu:

```bash
source venv/bin/activate
```

The terminal should now show something similar to:

```text
(venv) user@ubuntu:~/smart_attendance_project$
```

---

# 11. Install Django

With the virtual environment activated:

```bash
pip install django
```

Verify:

```bash
python -m django --version
```

---

# 12. Create the Django Project

From the project root:

```bash
django-admin startproject smart_attendance .
```

The `.` is important because it creates the Django project in the current directory.

The structure becomes:

```text
smart_attendance_project/
├── manage.py
├── smart_attendance/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── venv/
```

---

# 13. Understand manage.py

`manage.py` is the main command-line utility for the Django project.

Common commands include:

```bash
python manage.py runserver
```

```bash
python manage.py migrate
```

```bash
python manage.py makemigrations
```

```bash
python manage.py createsuperuser
```

---

# 14. Test the Initial Django Project

Run:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

The default Django welcome page should appear.

Stop the server:

```text
Ctrl + C
```

---

# 15. Create the Attendance Application

Create the app:

```bash
python manage.py startapp attendance
```

The project now contains:

```text
attendance/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

---

# 16. Register the Attendance App

Open:

```text
smart_attendance/settings.py
```

Find:

```python
INSTALLED_APPS = [
```

Add:

```python
'attendance',
```

Example:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'attendance',
]
```

Save the file.

---

# 17. Create the Templates Directory

From the project root:

```bash
mkdir -p templates/attendance
```

The structure should be:

```text
templates/
└── attendance/
```

---

# 18. Configure Django Templates

Open:

```text
smart_attendance/settings.py
```

In the `TEMPLATES` configuration, use:

```python
'DIRS': [BASE_DIR / 'templates'],
```

The relevant configuration should look like:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

---

# 19. Create index.html

Create:

```bash
touch templates/attendance/index.html
```

Correct location:

```text
smart_attendance_project/
└── templates/
    └── attendance/
        └── index.html
```

---

# 20. Create the Home View

Open:

```text
attendance/views.py
```

Add:

```python
from django.shortcuts import render


def home(request):
    return render(request, "attendance/index.html")
```

---

# 21. Create App URLs

Create:

```bash
touch attendance/urls.py
```

Add:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

Important: `attendance/urls.py` must be directly inside the `attendance` application.

Correct:

```text
attendance/
├── models.py
├── views.py
├── urls.py
└── admin.py
```

Not:

```text
attendance/
└── attendance/
    └── urls.py
```

---

# 22. Connect App URLs to the Main Project

Open:

```text
smart_attendance/urls.py
```

Use:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('attendance.urls')),
]
```

---

# 23. Create a Basic Test Page

Put this into:

```text
templates/attendance/index.html
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>Smart Attendance</title>
</head>
<body>

    <h1>Smart Attendance Monitoring System</h1>

    <p>Welcome to SmartAttend!</p>

</body>
</html>
```

Save the file.

---

# 24. Test the Application

Run:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

The page should display:

```text
Smart Attendance Monitoring System
Welcome to SmartAttend!
```

At this stage, Django routing, views, and templates are working.

---

# 25. Create Database Models

Open:

```text
attendance/models.py
```

A basic implementation can use:

```python
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.roll_number} - {self.name}"


class Attendance(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    date = models.DateField()
    subject = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student.name} - {self.date}"
```

The fields can be modified to match the final version of the application.

---

# 26. Create and Apply Migrations

After changing models:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

---

# 27. Register Models in Django Admin

Open:

```text
attendance/admin.py
```

Add:

```python
from django.contrib import admin
from .models import Student, Attendance

admin.site.register(Student)
admin.site.register(Attendance)
```

---

# 28. Create a Superuser

Run:

```bash
python manage.py createsuperuser
```

Enter the requested username, email, and password.

Run the server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/admin/
```

Log in with the superuser account.

---

# 29. Implement the Single-Page Dashboard

The main interface is:

```text
templates/attendance/index.html
```

The dashboard can contain:

- Project title
- Total students
- Present count
- Absent count
- Attendance percentage
- Student records
- Attendance records
- Forms/actions for attendance management

A conceptual layout is:

```text
+--------------------------------------------------+
|        SMART ATTENDANCE MONITORING               |
+--------------------------------------------------+
| Total Students | Present | Absent | Percentage  |
+--------------------------------------------------+
|                                                  |
| Attendance Records                               |
|                                                  |
| Roll No | Student | Date | Subject | Status     |
|---------|---------|------|---------|------------|
| 101     | Student | ...  | ...     | Present    |
+--------------------------------------------------+
```

---

# 30. Pass Database Data to the Template

A typical view can retrieve database records:

```python
from django.shortcuts import render
from .models import Student, Attendance


def home(request):
    students = Student.objects.all()
    attendance_records = Attendance.objects.all()

    context = {
        'students': students,
        'attendance_records': attendance_records,
    }

    return render(
        request,
        'attendance/index.html',
        context
    )
```

The template can display values with Django template syntax:

```html
{% for student in students %}
    <p>{{ student.name }}</p>
{% endfor %}
```

---

# 31. Attendance Status

In the example model:

```python
status = models.BooleanField(default=True)
```

The meaning is:

```text
True  → Present
False → Absent
```

Example:

```python
Attendance.objects.create(
    student=student,
    date=date,
    subject=subject,
    status=True
)
```

The actual form-processing implementation should follow the final project code.

---

# 32. Attendance Percentage

The attendance percentage is:

```text
Attendance Percentage =
(Present Classes / Total Classes) × 100
```

Example:

```text
Present = 18
Total = 20

Attendance = (18 / 20) × 100
           = 90%
```

This value can be calculated in the Django view and displayed on the dashboard.

---

# 33. Project Verification

Run:

```bash
python manage.py check
```

Then:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

Test the main application:

```text
http://127.0.0.1:8000/
```

Test the admin:

```text
http://127.0.0.1:8000/admin/
```

---

# 34. Troubleshooting

## 34.1 TemplateDoesNotExist

Error:

```text
TemplateDoesNotExist at /
attendance/index.html
```

Django should find:

```text
templates/attendance/index.html
```

Check:

```text
smart_attendance_project/
├── templates/
│   └── attendance/
│       └── index.html
```

Also check:

```python
'DIRS': [BASE_DIR / 'templates'],
```

And:

```python
return render(request, "attendance/index.html")
```

---

## 34.2 Pylance Cannot Resolve `from . import views`

If VS Code reports:

```text
Import "." could not be resolved
```

check that:

```text
attendance/
├── urls.py
└── views.py
```

are in the same directory.

Then select the correct Python interpreter in VS Code:

```text
Ctrl + Shift + P
→ Python: Select Interpreter
→ venv/bin/python
```

---

## 34.3 Django Command Not Found

If:

```bash
django-admin
```

is unavailable, activate the virtual environment:

```bash
source venv/bin/activate
```

Then:

```bash
pip install django
```

---

## 34.4 Port Already in Use

If port 8000 is occupied, use another port:

```bash
python manage.py runserver 8001
```

Open:

```text
http://127.0.0.1:8001/
```

---

# 35. Create requirements.txt

After the project is working:

```bash
pip freeze > requirements.txt
```

Check it:

```bash
cat requirements.txt
```

Another computer can install the same dependencies using:

```bash
pip install -r requirements.txt
```

---

# 36. Create .gitignore

Create:

```bash
touch .gitignore
```

Recommended contents:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
venv/
.venv/
env/

# Django
*.log
db.sqlite3
media/
staticfiles/

# Environment variables
.env
.env.*

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Python packaging
*.egg-info/
dist/
build/
```

This prevents unnecessary or sensitive files from being committed.

---

# 37. Security Check Before GitHub

Before making the repository public, inspect:

```text
smart_attendance/settings.py
```

Do not commit:

- Passwords
- API keys
- Authentication tokens
- Private credentials
- Production secret keys
- Other sensitive configuration

For production applications, sensitive settings should be supplied through environment variables or a secret-management system.

---

# 38. Initialize Git

From the project root:

```bash
git init -b main
```

Check:

```bash
git status
```

---

# 39. Configure Git Identity

If Git has not been configured:

```bash
git config --global user.name "YOUR NAME"
```

```bash
git config --global user.email "YOUR_GITHUB_EMAIL"
```

Verify:

```bash
git config --global --list
```

---

# 40. Create the GitHub Repository

Open GitHub and create a new repository.

Suggested name:

```text
smart-attendance-django
```

Suggested description:

```text
A single-page Smart Attendance Monitoring System developed using Django and SQLite.
```

For an existing local project, it is easiest to create the remote repository without automatically adding a README or other initial files.

---

# 41. Connect Local Git to GitHub

Copy the HTTPS repository URL.

Example:

```text
https://github.com/YOUR_USERNAME/smart-attendance-django.git
```

Add the remote:

```bash
git remote add origin https://github.com/YOUR_USERNAME/smart-attendance-django.git
```

Verify:

```bash
git remote -v
```

---

# 42. GitHub Authentication on Ubuntu

GitHub does not accept a normal account password for Git operations over HTTPS.

GitHub CLI provides a convenient browser-based authentication method.

Install GitHub CLI if required:

```bash
sudo apt update
sudo apt install gh -y
```

Check:

```bash
gh --version
```

Log in:

```bash
gh auth login
```

Select:

```text
GitHub.com
```

Then:

```text
HTTPS
```

Then:

```text
Login with a web browser
```

Complete authentication in the browser.

Check:

```bash
gh auth status
```

Configure Git:

```bash
gh auth setup-git
```

---

# 43. Create the Initial Git Commit

Check the files:

```bash
git status
```

Stage:

```bash
git add .
```

Check again:

```bash
git status
```

Make sure `venv/` and `db.sqlite3` are not being staged.

Commit:

```bash
git commit -m "Initial commit - Smart Attendance Monitoring System"
```

---

# 44. Push to GitHub

If the remote GitHub repository is empty:

```bash
git push -u origin main
```

Refresh the GitHub repository page.

The project files should now appear online.

---

# 45. If Push Is Rejected with `fetch first`

You may see:

```text
[rejected] main -> main (fetch first)
```

This usually means the GitHub repository already contains a commit, such as a README.

Run:

```bash
git pull origin main --allow-unrelated-histories --no-rebase
```

If the merge completes:

```bash
git push -u origin main
```

---

# 46. If Git Says "Need to Specify How to Reconcile Divergent Branches"

Use:

```bash
git pull origin main --allow-unrelated-histories --no-rebase
```

Then:

```bash
git push -u origin main
```

The `--no-rebase` option tells Git to merge the two histories.

---

# 47. If a Merge Conflict Occurs

Check:

```bash
git status
```

If a file such as `README.md` has a conflict, open it in VS Code.

Conflict markers may look like:

```text
<<<<<<< HEAD
Local content
=======
Remote content
>>>>>>> origin/main
```

Keep or combine the required content and remove the conflict markers.

Then:

```bash
git add .
```

```bash
git commit -m "Merge remote repository with local project"
```

Finally:

```bash
git push -u origin main
```

---

# 48. Normal Git Workflow After Setup

Whenever the project changes:

```bash
git status
```

Then:

```bash
git add .
```

Then:

```bash
git commit -m "Describe the change"
```

Then:

```bash
git push
```

Workflow:

```text
Modify Code
    |
    v
git status
    |
    v
git add .
    |
    v
git commit -m "message"
    |
    v
git push
    |
    v
GitHub
```

---

# 49. Recommended Commit Messages

Examples:

```bash
git commit -m "Add attendance models"
```

```bash
git commit -m "Create single-page dashboard"
```

```bash
git commit -m "Add student attendance form"
```

```bash
git commit -m "Improve dashboard styling"
```

```bash
git commit -m "Fix attendance calculation"
```

```bash
git commit -m "Update project documentation"
```

---

# 50. Final Repository Structure

The GitHub repository should approximately contain:

```text
smart-attendance-django/
│
├── attendance/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── smart_attendance/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│   └── attendance/
│       └── index.html
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

`venv/` and `db.sqlite3` should normally be excluded by `.gitignore`.

---

# 51. Reproduce the Project on Another Ubuntu Computer

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/smart-attendance-django.git
```

Enter the directory:

```bash
cd smart-attendance-django
```

Create the virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Create an administrator if required:

```bash
python manage.py createsuperuser
```

Run:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 52. Development Checklist

Before considering the project complete:

- [ ] Python installed
- [ ] pip installed
- [ ] Git installed
- [ ] Virtual environment created
- [ ] Virtual environment activated
- [ ] Django installed
- [ ] Django project created
- [ ] Attendance app created
- [ ] Attendance added to `INSTALLED_APPS`
- [ ] Templates directory created
- [ ] `index.html` created
- [ ] Template directory configured
- [ ] Home view created
- [ ] App URL configuration created
- [ ] Main URL configuration connected
- [ ] Models created
- [ ] Migrations created
- [ ] Migrations applied
- [ ] Admin configured
- [ ] Superuser created
- [ ] Single-page dashboard implemented
- [ ] Attendance functionality tested
- [ ] `python manage.py check` passes
- [ ] `requirements.txt` created
- [ ] `.gitignore` created
- [ ] Sensitive information checked
- [ ] Git initialized
- [ ] GitHub repository created
- [ ] GitHub authentication configured
- [ ] Remote added
- [ ] Initial commit created
- [ ] Project pushed to GitHub
- [ ] README added
- [ ] Documentation completed

---

# 53. Complete Development Flow

```text
Install Development Tools
          |
          v
Create Project Directory
          |
          v
Create Python Virtual Environment
          |
          v
Install Django
          |
          v
Create Django Project
          |
          v
Create Attendance App
          |
          v
Configure settings.py
          |
          v
Create Templates
          |
          v
Configure URLs
          |
          v
Create Views
          |
          v
Create Models
          |
          v
Run Migrations
          |
          v
Configure Django Admin
          |
          v
Build Single-Page Dashboard
          |
          v
Test Application
          |
          v
Create requirements.txt
          |
          v
Create .gitignore
          |
          v
Initialize Git
          |
          v
Create GitHub Repository
          |
          v
Authenticate GitHub
          |
          v
Commit Source Code
          |
          v
Push to GitHub
          |
          v
Document Project
          |
          v
       COMPLETE
```

---

# 54. Final Outcome

After completing this procedure, the project provides:

1. A Django-based web application.
2. A single-page attendance dashboard.
3. Database-backed attendance management.
4. Django Admin support.
5. Reproducible Python dependencies through `requirements.txt`.
6. Git-based version control.
7. A GitHub repository containing the source code.
8. Documentation for setting up and reproducing the project.

---

# 55. Author

**Ivan Antony Babu**

Electronics and Communication Engineering  
Cochin University of Science and Technology (CUSAT)

**Project:** Smart Attendance Monitoring System
