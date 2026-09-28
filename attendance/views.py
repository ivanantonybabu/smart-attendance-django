from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Count, Q
from .models import Student, Attendance


def home(request):

    # Add Student
    if request.method == "POST" and request.POST.get("action") == "add_student":

        name = request.POST.get("name")
        roll_number = request.POST.get("roll_number")
        department = request.POST.get("department")

        if name and roll_number and department:
            try:
                Student.objects.create(
                    name=name,
                    roll_number=roll_number,
                    department=department
                )
                messages.success(request, "Student added successfully!")
            except Exception:
                messages.error(request, "Roll number already exists.")

        return redirect("home")

    # Mark Attendance
    if request.method == "POST" and request.POST.get("action") == "mark_attendance":

        student_id = request.POST.get("student")
        date = request.POST.get("date")
        subject = request.POST.get("subject")
        status = request.POST.get("status")

        if student_id and date and subject and status:
            Attendance.objects.create(
                student_id=student_id,
                date=date,
                subject=subject,
                status=status
            )
            messages.success(request, "Attendance marked successfully!")

        return redirect("home")

    # Delete Attendance
    if request.method == "POST" and request.POST.get("action") == "delete_attendance":

        attendance_id = request.POST.get("attendance_id")
        attendance = get_object_or_404(Attendance, id=attendance_id)
        attendance.delete()

        messages.success(request, "Attendance record deleted!")
        return redirect("home")

    # Fetch all students
    students = Student.objects.all().order_by("roll_number")

    # Fetch attendance records
    attendance_records = Attendance.objects.select_related(
        "student"
    ).all().order_by("-date", "-id")

    # Statistics
    total_students = students.count()

    present_today = Attendance.objects.filter(
        status="Present"
    ).count()

    absent_today = Attendance.objects.filter(
        status="Absent"
    ).count()

    total_attendance = Attendance.objects.count()

    if total_attendance > 0:
        overall_percentage = round(
            (present_today / total_attendance) * 100, 2
        )
    else:
        overall_percentage = 0

    # Student attendance summary
    student_summary = []

    for student in students:

        total_classes = Attendance.objects.filter(
            student=student
        ).count()

        present_classes = Attendance.objects.filter(
            student=student,
            status="Present"
        ).count()

        absent_classes = Attendance.objects.filter(
            student=student,
            status="Absent"
        ).count()

        if total_classes > 0:
            percentage = round(
                (present_classes / total_classes) * 100, 2
            )
        else:
            percentage = 0

        student_summary.append({
            "student": student,
            "total_classes": total_classes,
            "present_classes": present_classes,
            "absent_classes": absent_classes,
            "percentage": percentage
        })

    context = {
        "students": students,
        "attendance_records": attendance_records,
        "student_summary": student_summary,
        "total_students": total_students,
        "present_today": present_today,
        "absent_today": absent_today,
        "overall_percentage": overall_percentage,
    }

    return render(request, "attendance/index.html", context)