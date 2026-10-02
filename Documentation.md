
# SMART ATTENDANCE MONITORING SYSTEM

The **Smart Attendance Monitoring System** is a Django-based web application developed to digitally manage and monitor student attendance. The project provides a simple single-page dashboard through which attendance information can be viewed and managed.

The project is implemented using **Python, Django, HTML, CSS and SQLite**.

---

## TABLE OF CONTENTS

1. [Home Page](#home-page)
2. [Django Project Structure](#django-project-structure)
3. [Development Environment](#development-environment)
4. [Project Creation](#project-creation)
5. [Virtual Environment](#virtual-environment)
6. [Installing Django](#installing-django)
7. [Creating The Django Project](#creating-the-django-project)
8. [Running The Initial Project](#running-the-initial-project)
9. [Creating The Attendance Application](#creating-the-attendance-application)
10. [Registering The Application](#registering-the-application)
11. [Template Configuration](#template-configuration)
12. [Home Page View](#home-page-view)
13. [Url Configuration](#url-configuration)
14. [Single Page Interface](#single-page-interface)
15. [Attendance Database](#attendance-database)
16. [Attendance Model](#attendance-model)
17. [Database Migration](#database-migration)
18. [Sqlite Database](#sqlite-database)
19. [Django Admin](#django-admin)
20. [Admin User](#admin-user)
21. [Attendance Dashboard](#attendance-dashboard)
22. [Attendance Statistics](#attendance-statistics)
23. [View With Database Data](#view-with-database-data)
24. [Displaying Data In Html](#displaying-data-in-html)
25. [How To Test And Use The Interface](#how-to-test-and-use-the-interface)
26. [Project Testing](#project-testing)
27. [Common Error — Templatedoesnotexist](#common-error-templatedoesnotexist)
28. [Common Error — Import Could Not Be Resolved](#common-error-import-could-not-be-resolved)
29. [Project Requirements](#project-requirements)
30. [Github Version Control](#github-version-control)
31. [Gitignore](#gitignore)
32. [Github Repository](#github-repository)
33. [Connecting Local Project To Github](#connecting-local-project-to-github)
34. [Github Authentication](#github-authentication)
35. [First Commit](#first-commit)
36. [Pushing To Github](#pushing-to-github)
37. [Fetch First Error](#fetch-first-error)
38. [Divergent Branch Error](#divergent-branch-error)
39. [Normal Github Workflow](#normal-github-workflow)
40. [Final Project Workflow](#final-project-workflow)
41. [Author](#author)

---



# HOME PAGE

The home page acts as the main interface of the Smart Attendance Monitoring System.

It can contain:

- Project title
- Total number of students
- Number of students present
- Number of students absent
- Overall attendance percentage
- Attendance records
- Attendance entry controls

The complete interface is designed as a **single-page dashboard**, so the main information can be accessed without navigating through multiple pages.





# DJANGO PROJECT STRUCTURE

The project is organized using the standard Django structure.

```text
smart_attendance_project/
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
├── manage.py
├── requirements.txt
├── README.md
├── SETUP.md
└── .gitignore
```

---

# DEVELOPMENT ENVIRONMENT

The project was developed on Ubuntu using Visual Studio Code.

### Required software

```bash
python3
pip
python3-venv
git
visual-studio-code
```

Check the installed versions:

```bash
python3 --version
pip3 --version
git --version
```

---

# PROJECT CREATION

Create the project directory:

```bash
mkdir smart_attendance_project
cd smart_attendance_project
```

Open it in VS Code:

```bash
code .
```

---

# VIRTUAL ENVIRONMENT

A Python virtual environment is created so that the Django dependencies remain isolated from the system Python installation.

Create the environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

After activation, the terminal should display:

```text
(venv) user@ubuntu:~/smart_attendance_project$
```

---

# INSTALLING DJANGO

Install Django:

```bash
pip install django
```

Verify the installation:

```bash
python -m django --version
```

---

# CREATING THE DJANGO PROJECT

Create the Django project:

```bash
django-admin startproject smart_attendance .
```

This creates:

```text
smart_attendance/
├── __init__.py
├── settings.py
├── urls.py
├── asgi.py
└── wsgi.py
```

The main project management file is:

```text
manage.py
```

---

# RUNNING THE INITIAL PROJECT

Start the Django development server:

```bash
python manage.py runserver
```

Open the browser:

```text
http://127.0.0.1:8000/
```

The default Django page confirms that the Django project has been configured correctly.

Stop the server using:

```text
Ctrl + C
```

---

# CREATING THE ATTENDANCE APPLICATION

Create the application:

```bash
python manage.py startapp attendance
```

The attendance application contains the main application logic.

```text
attendance/
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

---

# REGISTERING THE APPLICATION

Open:

```text
smart_attendance/settings.py
```

Add the attendance application to `INSTALLED_APPS`:

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

---

# TEMPLATE CONFIGURATION

Create the template directory:

```bash
mkdir -p templates/attendance
```

Create:

```text
templates/attendance/index.html
```

In `settings.py`, configure the template directory:

```python
'DIRS': [BASE_DIR / 'templates'],
```

The Django template engine can now locate:

```text
templates/attendance/index.html
```

---

# HOME PAGE VIEW

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

The `home()` function receives the browser request and returns the main HTML page.

---

# URL CONFIGURATION

Create:

```text
attendance/urls.py
```

Add:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

Then open:

```text
smart_attendance/urls.py
```

Configure:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('attendance.urls')),
]
```

The URL flow is:

```text
Browser
   |
   v
/
   |
   v
smart_attendance/urls.py
   |
   v
attendance/urls.py
   |
   v
views.home()
   |
   v
attendance/index.html
```

---

# SINGLE PAGE INTERFACE

The main interface is implemented in:

```text
templates/attendance/index.html
```

A basic page structure is:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Smart Attendance</title>
</head>

<body>

    <h1>Smart Attendance Monitoring System</h1>

    <p>Attendance Dashboard</p>

</body>
</html>
```

The HTML can then be expanded with CSS cards, tables, forms and statistics.

---

# ATTENDANCE DATABASE

The project uses Django models to store student and attendance information.

Open:

```text
attendance/models.py
```

Example student model:

```python
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(
        max_length=50,
        unique=True
    )
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.roll_number} - {self.name}"
```

The model stores:

| Field | Purpose |
|---|---|
| name | Student name |
| roll_number | Unique student identifier |
| department | Student department |

---

# ATTENDANCE MODEL

The attendance model stores individual attendance records.

```python
class Attendance(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    subject = models.CharField(
        max_length=100
    )

    status = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.student.name} - {self.date}"
```

The database relationship is:

```text
Student
   |
   | 1
   |
   |----< Attendance
             |
             +-- Date
             +-- Subject
             +-- Status
```

---

# DATABASE MIGRATION

After creating or modifying models:

```bash
python manage.py makemigrations
```

Apply the migrations:

```bash
python manage.py migrate
```

Django creates the required SQLite database tables.

---

# SQLITE DATABASE

The default Django database is SQLite.

The database file is:

```text
db.sqlite3
```

SQLite is suitable for this academic project because it does not require a separate database server.

The database configuration is maintained in:

```text
smart_attendance/settings.py
```

---

# DJANGO ADMIN

The Django Admin interface can be used to manage student and attendance records.

Open:

```text
attendance/admin.py
```

Register the models:

```python
from django.contrib import admin
from .models import Student, Attendance

admin.site.register(Student)
admin.site.register(Attendance)
```

---

# ADMIN USER

Create a superuser:

```bash
python manage.py createsuperuser
```

Run the server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/admin/
```

The administrator can use the Django Admin interface to create and manage student and attendance data.

---

# ATTENDANCE DASHBOARD

The dashboard can display the following information:

```text
+-------------------------------------------------------+
|          SMART ATTENDANCE MONITORING SYSTEM           |
+-------------------------------------------------------+
|                                                       |
| Total Students | Present | Absent | Attendance %     |
|       50       |   42    |   8    |      84%         |
|                                                       |
+-------------------------------------------------------+
| ATTENDANCE RECORDS                                    |
+-------------------------------------------------------+
| Roll No | Student | Date | Subject | Status           |
|---------|---------|------|---------|------------------|
| 101     | Student | ...  | ...     | Present          |
| 102     | Student | ...  | ...     | Absent           |
+-------------------------------------------------------+
```

---

# ATTENDANCE STATISTICS

The attendance percentage can be calculated using:

```text
Attendance Percentage =
(Present Classes / Total Classes) × 100
```

For example:

```text
Present Classes = 18
Total Classes   = 20

Attendance Percentage =
(18 / 20) × 100

= 90%
```

These values can be calculated in the Django view and passed to the template.

---

# VIEW WITH DATABASE DATA

The home view can retrieve database information:

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

---

# DISPLAYING DATA IN HTML

Django template syntax can be used to display database records.

Example:

```html
{% for student in students %}

    <p>
        {{ student.roll_number }}
        -
        {{ student.name }}
    </p>

{% endfor %}
```

Attendance records can similarly be displayed:

```html
{% for record in attendance_records %}

    <p>
        {{ record.student.name }}
        -
        {{ record.date }}
        -
        {{ record.subject }}
    </p>

{% endfor %}
```

---


# HOW TO TEST AND USE THE INTERFACE

After completing the Django implementation, the project can be tested directly through the web browser.

## 1. Start the Django Server

Open the terminal in the project directory:

```bash
cd ~/smart_attendance_project
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Start Django:

```bash
python manage.py runserver
```

You should see:

```text
Starting development server at http://127.0.0.1:8000/
```

---

## 2. Open the Main Interface

Open a browser and visit:

```text
http://127.0.0.1:8000/
```

This is the main interface of the **Smart Attendance Monitoring System**.

The page should display the single-page attendance dashboard.

---

## 3. What to Check on the Interface

The dashboard should provide the main attendance information in one page.

For example:

```text
+------------------------------------------------------+
|       SMART ATTENDANCE MONITORING SYSTEM             |
+------------------------------------------------------+
|                                                      |
|  TOTAL STUDENTS     PRESENT     ABSENT     ATTENDANCE|
|       50               42          8          84%    |
|                                                      |
+------------------------------------------------------+
|                 ATTENDANCE RECORDS                   |
+------------------------------------------------------+
| Roll No | Name | Date | Subject | Status             |
|---------|------|------|---------|--------------------|
| 101     | A    | ...  | IoT     | Present            |
| 102     | B    | ...  | IoT     | Present            |
| 103     | C    | ...  | IoT     | Absent             |
+------------------------------------------------------+
```

Check that:

- The page loads without an error.
- The project title is visible.
- Attendance statistics are displayed.
- Student/attendance records are visible.
- Present and absent statuses are shown correctly.
- The attendance percentage is displayed correctly.
- The page remains a single-page interface.

---

## 4. Add Data Through Django Admin

Open another browser tab:

```text
http://127.0.0.1:8000/admin/
```

Log in using the superuser credentials.

Add sample students and attendance records through the Admin interface.

For example:

```text
Student:
Roll Number: 101
Name: Student One
Department: ECE
```

Then create an attendance record:

```text
Student: Student One
Date: 28-09-2026
Subject: IoT
Status: Present
```

---

## 5. Return to the Main Interface

Go back to:

```text
http://127.0.0.1:8000/
```

Refresh the page.

The newly added information should now appear in the dashboard.

This verifies that:

```text
Django Admin
     |
     v
SQLite Database
     |
     v
Django Model
     |
     v
Django View
     |
     v
HTML Template
     |
     v
Browser Dashboard
```

---

## 6. Test Different Attendance Values

Add several attendance records with different statuses.

For example:

```text
Student One  → Present
Student Two  → Present
Student Three → Absent
Student Four → Present
```

Refresh the dashboard and verify that the displayed attendance statistics change according to the database records.

---

## 7. Final Interface Test

The project is ready for demonstration when:

```text
Browser
   ↓
http://127.0.0.1:8000/
   ↓
Smart Attendance Dashboard
   ↓
Student / Attendance Information
   ↓
Statistics
```

works without errors.


# PROJECT TESTING

Check the Django project:

```bash
python manage.py check
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

Main page:

```text
http://127.0.0.1:8000/
```

Admin page:

```text
http://127.0.0.1:8000/admin/
```

---

# COMMON ERROR — TEMPLATEDOESNOTEXIST

If Django displays:

```text
TemplateDoesNotExist at /
attendance/index.html
```

verify that the file exists at:

```text
templates/
└── attendance/
    └── index.html
```

Verify `settings.py`:

```python
'DIRS': [BASE_DIR / 'templates'],
```

Verify the view:

```python
return render(request, "attendance/index.html")
```

All three locations must match.

---

# COMMON ERROR — IMPORT COULD NOT BE RESOLVED

If VS Code displays:

```text
Import "." could not be resolved
```

check that:

```text
attendance/
├── urls.py
└── views.py
```

are in the same application directory.

Then select the virtual environment in VS Code:

```text
Ctrl + Shift + P
→ Python: Select Interpreter
→ venv/bin/python
```

---

# PROJECT REQUIREMENTS

Create the dependency file:

```bash
pip freeze > requirements.txt
```

This allows the project dependencies to be reproduced on another computer.

Install them later using:

```bash
pip install -r requirements.txt
```

---

# GITHUB VERSION CONTROL

Git is used to maintain the source-code history.

Initialize Git:

```bash
git init -b main
```

Check the repository:

```bash
git status
```

---

# GITIGNORE

Create:

```text
.gitignore
```

Recommended contents:

```gitignore
venv/
.venv/
__pycache__/
*.py[cod]
db.sqlite3
*.log
.env
.vscode/
.idea/
staticfiles/
media/
```

The virtual environment and local database should not normally be uploaded to GitHub.

---

# GITHUB REPOSITORY

Create a repository on GitHub.

Suggested repository name:

```text
smart-attendance-django
```

Suggested description:

```text
A single-page Smart Attendance Monitoring System developed using Django and SQLite.
```

---

# CONNECTING LOCAL PROJECT TO GITHUB

Add the GitHub remote:

```bash
git remote add origin https://github.com/YOUR_USERNAME/smart-attendance-django.git
```

Verify:

```bash
git remote -v
```

---

# GITHUB AUTHENTICATION

GitHub does not accept a normal account password for Git operations over HTTPS.

GitHub CLI can be used for authentication.

Install:

```bash
sudo apt update
sudo apt install gh -y
```

Login:

```bash
gh auth login
```

Select:

```text
GitHub.com
HTTPS
Login with a web browser
```

After authentication:

```bash
gh auth setup-git
```

Check:

```bash
gh auth status
```

---

# FIRST COMMIT

Check the files:

```bash
git status
```

Stage the project:

```bash
git add .
```

Create the first commit:

```bash
git commit -m "Initial commit - Smart Attendance Monitoring System"
```

---

# PUSHING TO GITHUB

Push the project:

```bash
git push -u origin main
```

After a successful push, refresh the GitHub repository page.

The source code and documentation will be available in the repository.

---

# FETCH FIRST ERROR

If GitHub returns:

```text
[rejected] main -> main (fetch first)
```

the remote repository already contains commits that are not available locally.

Use:

```bash
git pull origin main --allow-unrelated-histories --no-rebase
```

Then:

```bash
git push -u origin main
```

---

# DIVERGENT BRANCH ERROR

If Git reports:

```text
Need to specify how to reconcile divergent branches
```

use:

```bash
git pull origin main --allow-unrelated-histories --no-rebase
```

Then push:

```bash
git push -u origin main
```

---

# NORMAL GITHUB WORKFLOW

After the project has been connected to GitHub, use:

```bash
git status
```

```bash
git add .
```

```bash
git commit -m "Describe the change"
```

```bash
git push
```

The complete workflow is:

```text
Edit Project
     |
     v
git status
     |
     v
git add .
     |
     v
git commit
     |
     v
git push
     |
     v
GitHub Repository
```

---



# FINAL PROJECT WORKFLOW

```text
Ubuntu
   |
   v
Python
   |
   v
Virtual Environment
   |
   v
Django
   |
   v
Django Project
   |
   v
Attendance App
   |
   +------------------+
   |                  |
   v                  v
Models              Views
   |                  |
   v                  v
SQLite             Templates
   |                  |
   +--------+---------+
            |
            v
     Single Page Dashboard
            |
            v
       Project Testing
            |
            v
           Git
            |
            v
         GitHub
```

---

#

# AUTHOR

**Ivan Antony Babu**

Electronics and Communication Engineering  
Cochin University of Science and Technology (CUSAT)

**Project:** Smart Attendance Monitoring System

**Framework:** Django

**Database:** SQLite

**Platform:** Ubuntu Linux
