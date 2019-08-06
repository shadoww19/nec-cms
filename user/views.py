from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import User, Marks
from .forms import LoginForm, RegisterForm, MarksForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            collegeId = form.cleaned_data['collegeId']
            password = form.cleaned_data['password']
            userList = User.objects.filter(collegeId = collegeId, password = password).values()
            User.objects.filter(collegeId = collegeId).update(isLoggedIn = 1)
            user = list(userList)[0]
            if user['role'] == 'hod':
                return render(request, 'dashboard_hod.html', {"user": user})
            elif user['role'] == 'teacher':
                return render(request, 'dashboard_teacher.html', {"user": user})
            elif user['role'] == 'student':
                query = User.objects.filter(collegeId=collegeId).values()
                student = list(query)[0]
                q = User.objects.get(collegeId = student['collegeId'])
                query1 = Marks.objects.filter(student = q).values()
                if len(list(query1)) == 0:
                    subjects = []
                    marks= 0
                    percent = 0
                else:
                    subjects = list(query1)[0]
                    marks = subjects['subject1'] + subjects['subject2'] + subjects['subject3']
                    percent = (marks / 300) * 100
                student = {"name": student['name'], "email": student['email'], "collegeId": student['collegeId'], "marks": marks, "percent": percent, "subjects": subjects}
                return render(request, 'dashboard_student.html', {"student": student})
                
    elif request.method == 'GET':
        return render(request, 'login.html')

def logout(request):
    if request.method == 'GET':
        collegeId = request.GET.get('collegeId')
        query = User.objects.filter(collegeId = collegeId).update(isLoggedIn=0)
        return HttpResponseRedirect("/user/login")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
            count = User.objects.filter(role = role).values().count()
            count += 1
            collegeId=''
            if role == 'teacher':
                collegeId = 'FAC' + str(count)
            if role == 'hod':
                collegeId = 'HOD' + str(count)
            if role == 'student':
                collegeId = 'STU' + str(count)
            User.objects.create(name=name, email=email, password=password, role = role, collegeId = collegeId)
            return render(request, 'login.html')

    elif request.method == 'GET':
        return render(request, 'register.html')

def hod_dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard_hod.html')

def teacher_dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard_teacher.html')

def student_dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard_student.html')

def enter_marks(request):
    if request.method == 'GET':
        return render(request, 'marksForm.html')   

def get_teachers(request):
    if request.method == 'GET':
        query = User.objects.filter(role='teacher').values()
        teachers = list(query)
        return render(request, 'teacher_list.html', {"teachers": teachers})        

def get_students(request):
    if request.method == 'GET':
        studentquery = User.objects.filter(role='student').values()
        students = list(studentquery)
        return render(request, 'student_list.html', {"students": students})

def get_student(request):
    if request.method == 'GET':
        collegeId = request.GET.get('collegeId')
        query = User.objects.filter(collegeId=collegeId).values()
        student = list(query)[0]
        q = User.objects.get(collegeId = student['collegeId'])
        query1 = Marks.objects.filter(student = q).values()
        if len(list(query1)) == 0:
            subjects = []
            marks= 0
            percent = 0
        else:
            subjects = list(query1)[0]
            marks = subjects['subject1'] + subjects['subject2'] + subjects['subject3']
            percent = (marks / 300) * 100
        student = {"name": student['name'], "email": student['email'], "collegeId": student['collegeId'], "marks": marks, "percent": percent, "subjects": subjects}
        return render(request, 'student_details.html', {"student": student})

def add_marks(request):
    if request.method == 'GET':
        collegeId = request.GET.get('collegeId')
        query = User.objects.filter(collegeId=collegeId).values()
        student = list(query)[0]
        return render(request, 'marksForm.html', {"student": student})
    elif request.method == 'POST':
        form = MarksForm(request.POST)
        print(request.body)
        if form.is_valid():
            subject1 = form.cleaned_data['subject1']
            subject2 = form.cleaned_data['subject2']
            subject3 = form.cleaned_data['subject3']
            collegeId = request.GET.get('collegeId')
            student = User.objects.get(collegeId = collegeId)
            query = Marks.objects.create(subject1 = subject1, subject2 = subject2, subject3 = subject3, student = student)
            return HttpResponseRedirect('/user/dashboard/teacher/students')

def edit_marks(request):
    if request.method == 'GET':
        collegeId = request.GET.get('collegeId')
        query = User.objects.filter(collegeId=collegeId).values()
        student = list(query)[0]
        q = User.objects.get(collegeId = student['collegeId'])
        query1 = Marks.objects.filter(student = q).values()
        subjects = list(query1)[0]
        student = {"name": student['name'], "email": student['email'], "collegeId": student['collegeId'], "subjects": subjects}
        return render(request, 'editMarks.html', {"student": student})
    elif request.method == 'POST':
        form = MarksForm(request.POST)
        print(request.body)
        if form.is_valid():
            subject1 = form.cleaned_data['subject1']
            subject2 = form.cleaned_data['subject2']
            subject3 = form.cleaned_data['subject3']
            collegeId = request.GET.get('collegeId')
            print
            student = User.objects.get(collegeId = collegeId)
            query = Marks.objects.filter(student = student).update(subject1 = subject1, subject2 = subject2, subject3 = subject3)
            return HttpResponseRedirect('/user/dashboard/teacher/students')