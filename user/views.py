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
            user = list(userList)[0]
            if user['role'] == 'hod':
                return HttpResponseRedirect('/user/dashboard/hod')
            elif user['role'] == 'teacher':
                return HttpResponseRedirect('/user/dashboard/teacher')
            elif user['role'] == 'student':
                return render(request, 'dashboard_student.html', {"user":user})
                # return HttpResponseRedirect('/user/dashboard/student')
    elif request.method == 'GET':
        return render(request, 'login.html')

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
                collegeId = 'FAC' + str(count)
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