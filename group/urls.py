from django.contrib import admin
from django.urls import path
from group import views

'''
    'name=' is used for reverse linking which is efficient for dynamic routing
'''
urlpatterns = [
    path('', views.Signup_View.as_view(), name='home'),
    path('index',views.Index.as_view(),name='index'),

    path('login', views.Login_view.as_view(), name='login'),
    path('logout', views.Logout_view.as_view(), name='logout'),
    path('signup', views.Signup_View.as_view(), name='signup'),
    path('teacher-form', views.teacher_form_view.as_view(), name='teacher-form'), #create form by teacher
    path('formlisting', views.StudentFormListing.as_view(), name='formlisting'), #show list of available form
   path('formlisting/<str:title>', views.Question_Form.as_view(), name='formdetailpage'),
    # path('student-skill', views.Question_Form.as_view(), name='student-skill'),
    path('team-generator', views.Team_Generator.as_view(), name='team-generator'),

    #working
    path('question-form', views.Question_Form.as_view(), name='question-form'),

    path('student-profile', views.Student_Profile.as_view(), name='student-profile'),
    
    #review left


    # path('student-form', views.formdetailview.as_view(), name='student-form'),

    # path('student-profile', views.Student_Profile_view.as_view(), name='student-profile'),

    # path('team-generator', views.Team_generator.as_view(), name='team-generator'),

    # path('student-index', views.student_index.as_view(), name='student-index'),//student homepage
]