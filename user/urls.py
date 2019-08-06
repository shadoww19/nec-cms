from django.conf.urls import url
from user.views import login, logout, register, hod_dashboard, teacher_dashboard, student_dashboard, enter_marks, get_students, get_student, add_marks, edit_marks, get_teachers

urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^register/$', register, name="register"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^dashboard/hod/$', hod_dashboard, name="hod_dashboard"),
    url(r'^dashboard/teacher/$', teacher_dashboard, name="teacher_dashboard"),
    url(r'^dashboard/student/$', student_dashboard, name="student_dashboard"),
    url(r'^dashboard/teacher/marks/$',enter_marks, name='enter_marks'),
    url(r'^dashboard/teacher/students/$',get_students, name='student_list'),
    url(r'^dashboard/teacher/students/details/$',get_student, name='student_details'),
    url(r'^dashboard/students/add_marks/$', add_marks, name='add_marks'),
    url(r'^dashboard/students/edit_marks/$', edit_marks, name='edit_marks'),
    url(r'^dashboard/hod/teachers/$',get_teachers, name='teacher_list')    
]