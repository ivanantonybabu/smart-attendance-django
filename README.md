# Smart Attendance Monitoring System

A simple web-based **Smart Attendance Monitoring System** developed using the **Django framework**. The project provides a single-page interface for managing student attendance and viewing attendance information in an organized manner.

---

## 📌 Project Overview

The Smart Attendance Monitoring System is designed to digitize the basic process of recording and monitoring student attendance.

Instead of maintaining attendance manually, the application provides a centralized web interface where attendance-related information can be managed through Django.

The project was developed as a Django web development assignment using **Python, Django, HTML, CSS, and SQLite**.

---

## ✨ Features

- 📊 Single-page attendance dashboard
- 👨‍🎓 Student attendance management
- ✅ Mark students as Present or Absent
- 📋 View attendance records
- 📈 Attendance percentage monitoring
- 🗃️ Database-backed data storage
- 🌐 Django-based web interface
- 🛠️ Django Admin support
- 💻 Designed and developed on Ubuntu using Visual Studio Code

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web application framework |
| SQLite | Database |
| HTML5 | Webpage structure |
| CSS3 | User interface styling |
| Bootstrap | Responsive interface styling (if enabled) |
| Git | Version control |
| GitHub | Source-code hosting |
| Ubuntu | Development environment |
| Visual Studio Code | Development IDE |

---

## 🏗️ Project Architecture

The project follows Django's **Model-View-Template (MVT)** architecture.

```text
                User
                 │
                 ▼
        ┌─────────────────┐
        │  HTML Interface │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │   Django URLs   │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │   Django Views  │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Django Models   │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ SQLite Database │
        └─────────────────┘
```

---

## 📂 Project Structure

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
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---



## 👨‍💻 Author

**Ivan Antony Babu**

Electronics and Communication Engineering  
Cochin University of Science and Technology (CUSAT)

---

## 📄 License

This project was developed for academic and educational purposes.

You may modify and extend the project for learning and development.
