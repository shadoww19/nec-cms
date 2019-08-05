from django.conf.urls import url
from user.views import login, register, hod_dashboard, teacher_dashboard, student_dashboard, enter_marks

urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^register/$', register, name="register"),
    url(r'^dashboard/hod/$', hod_dashboard, name="hod_dashboard"),
    url(r'^dashboard/teacher/$', teacher_dashboard, name="teacher_dashboard"),
    url(r'^dashboard/student/$', student_dashboard, name="student_dashboard"),
    url(r'^dashboard/teacher/marks/$',enter_marks, name='enter_marks'),
]