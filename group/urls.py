from django.contrib import admin
from django.urls import path
from group import views

'''
    'name=' is used for reverse linking which is efficient for dynamic routing
'''
urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('index',views.Index.as_view(),name='index'),

    path('login', views.Login_view.as_view(), name='login'),
    path('logout', views.Logout_view.as_view(), name='logout'),
    path('signup', views.Signup_View.as_view(), name='signup'),
    
    path('teacher', views.teacher_form_view.as_view(), name='teacher'),
    path('student', views.student_form_view.as_view(), name='student'),
]