from django.shortcuts import render, redirect,HttpResponse

from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from django.template import loader
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from group.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import pandas as pd
import os

import questionaries 


# from django.template import loader
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.decorators import login_required
# from django.urls import reverse_lazy

class Index(View):
    def get(self,request):
        alert_title = request.session.get('alert_title',False)
        alert_detail = request.session.get('alert_detail',False)
        if(alert_title):del(request.session['alert_title'])
        if(alert_detail):del(request.session['alert_detail'])
        context = {
            'alert_title': alert_title,
            'alert_detail': alert_detail,
            "page_name":"Home"
        }
        try:
            if request.user.is_anonymous:
                return redirect("/login")
            elif not request.user.is_staff and not request.user.is_superuser:
                return render(request,"student_index.html",context)
            elif not request.user.is_superuser and request.user.is_staff:
                return render (request,"teacher_index.html",context)
            else :
                request.session['alert_title'] = "Invalid Access Attempt"
                request.session['alert_detail'] = "User is not Granted Acess."
                return redirect("/login")
        except Exception as e:
            pass
            
class Logout_view(View):
    def get(self,request):
        request.session.clear()
        logout(request)
        return redirect('/')
      
class Login_view(View):
    def get(self,request):
        alert_title = request.session.get('alert_title',False)
        alert_detail = request.session.get('alert_detail',False)
        if(alert_title):del(request.session['alert_title'])
        if(alert_detail):del(request.session['alert_detail'])
        context = {
            'alert_title': alert_title,
            'alert_detail': alert_detail,
            'page_name': 'login'
        }
        return render(request,"signin.html",context)
    
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = authenticate(username = username, password = password)
            if user is not None:# checks if the user is logged in or not?
                login(request,user) #logins the user
                return redirect ('/')
            else:
                request.session['alert_title'] = "Invalid Login Attempt"
                request.session['alert_detail'] = "Please enter valid login credential."
                return redirect(request.path)
        except Exception as e:
            request.session['alert_title'] = "Invalid Login Attempt"
            request.session['alert_detail'] = "Please enter valid login credential."
            return redirect(request.path)
      
class Signup_View (View):
    def get(self,request):
        alert_title = request.session.get('alert_title',False)
        alert_detail = request.session.get('alert_detail',False)
        if(alert_title):del(request.session['alert_title'])
        if(alert_detail):del(request.session['alert_detail'])
        context = {
            'alert_title':alert_title,
            'alert_detail':alert_detail,
            'page_name': 'Signup'
        }
        return render(request,"signup.html",context)
        
    def post(self,request):
        if request.method == 'POST':
            firstName = request.POST.get('firstName')
            lastName = request.POST.get('lastName')
            username = request.POST.get('username')  

            email = request.POST.get('email')
            password = request.POST.get('password')
            status  = request.POST.get('staff')

            # Email Validation
            try:
                validator = EmailValidator()
                validator(email)
            except ValidationError as e:
                request.session['alert_title'] = "Invalid Email"
                request.session['alert_detail'] = "Please enter valid email."
                return redirect(request.path)

            # Determine user type
            is_superuser = False
            is_staff = False
            if status == 'admin':
                is_superuser = True
                is_staff = True
            elif status == 'teacher':
                is_superuser = False
                is_staff = True
            elif status == 'student':
                is_superuser = False
                is_staff = False
                
            try:# Create user with validation
                user = User.objects.create_user(username, email, password, is_superuser=is_superuser, is_staff=is_staff)
                user.first_name = firstName
                user.last_name = lastName
                user.save()
            except Exception as e:
                request.session['alert_title'] = "Registration Fail"
                request.session['alert_detail'] = e
                return redirect(request.path)
                
            try:# Authenticate and Login
                user = authenticate(username=username, password=password)
                if user is not None:# checks if the user is logged in or not?
                    login(request,user) #logins the user
                    return redirect ('/')
                else:
                    # Handle failed authentication (e.g., display error message)
                    request.session['alert_title'] = "Login Fail"
                    request.session['alert_detail'] = "Invalid Attempt to login"
                    return redirect(request.path)
            except Exception as e:
                request.session['alert_title'] = "Registration Fail"
                request.session['alert_detail'] = e
                return redirect(request.path)
        return render(request, "signup.html")

class teacher_form_view(View): #creates form
    def get(self,request):
        context = {
            'page_name':'teacher-form'
        }
        return render(request,"teacher-form.html",context)
    def post(self,request):
        if request.method == 'POST':
            user_id = request.user.id
            title = request.POST.get('project-title')
            description = request.POST.get('project-description')

            communication = request.POST.get('communication') is not None
            presentation = request.POST.get('presentation') is not None
            coding = request.POST.get('coding') is not None
            leadership = request.POST.get('leadership') is not None
            form_detail = FormDetail.objects.create(
                user_id = user_id,
                title = title,
                description = description,
                communication=communication,
                presentation = presentation,
                coding = coding,
                leadership = leadership,
            ).save() 
        
        return redirect ('/')  
    
class StudentFormListing(View): #list open form
    def get(self, request):
        alert_title = request.session.get('alert_title', False)
        alert_detail = request.session.get('alert_detail', False)
        if alert_title:
            del request.session['alert_title']
        if alert_detail:
            del request.session['alert_detail']
        form_id = FormDetail.objects.all()
        context = {
            'alert_title': alert_title,
            'alert_detail': alert_detail,
            'page_name': 'student-form',
            'form_id': form_id
        }
        return render(request, "formlisting.html", context)
        
    def post(self,request):
        pass

'''class formdetailview(View):
    def get(self, request, title):
        formsingle = get_object_or_404(FormDetail, title=title)
        template = loader.get_template('student-form.html')
        context = {
            'formsingle': formsingle,
            'page_name' : 'form-details'
        }
        return HttpResponse(template.render(context, request))

    def post(self,request):
        if request.method == 'POST':
            user_id = request.user.id
            email = request.user.email if request.user.email else request.user.username
            name = request.user.username

            title = request.POST.get('form_id')
            communication = request.POST.get('communication')
            presentation = request.POST.get('presentation')
            coding = request.POST.get('coding')
            leadership = request.POST.get('leadership')
            try:
                student_detail = Skillset.objects.create(
                    user_id=user_id,
                    title=title,
                    communication=communication,
                    presentation=presentation,
                    coding=coding,
                    leadership=leadership,
                )
                if student_detail:
                    df = pd.DataFrame.from_dict([{
                        "user_id": student_detail.user_id,
                        "name" : name,
                        "email" : email,
                        "coding": student_detail.coding,
                        "leadership": student_detail.leadership,
                        "communication": student_detail.communication,
                        "presentation": student_detail.presentation,
                    }])
                    name = f"data/data.csv"
                    df.to_csv(name, mode='a', header=not os.path.exists(name), index=False, lineterminator='\n')

                student_detail.save()
                return redirect('/')
            except Exception as e:
                print(e)
        return redirect ('/')  '''

class student_form_view(View):
    def get(self,request):
        alert_title = request.session.get('alert_title',False)
        alert_detail = request.session.get('alert_detail',False)
        if(alert_title):del(request.session['alert_title'])
        if(alert_detail):del(request.session['alert_detail'])
        form_id = FormDetail.request.object()
        context = {
            'alert_title':alert_title,
            'alert_detail':alert_detail,
            'page_name': 'student-form',
            'form_id': form_id
        }
        return render(request,"student-form.html",context)
        
    def post(self,request):
        if request.method == 'POST':
            filename = request.POST.get('filename')
            user_id = request.user.id
            communication = request.POST.get('communication')
            presentation = request.POST.get('presentation')
            coding = request.POST.get('coding')
            leadership = request.POST.get('leadership')
            skillsets = Skillset.objects.create(
                user_id = user_id,
                coding = coding,
                leadership = leadership,
                communication=communication,
                presentation = presentation,
            ).save()  
            df = pd.DataFrame.from_dict(skillsets)
            filename = ''.csv
            df.to_csv(filename, index=False)
        return redirect ('/')  

class Student_Profile(View):
    def get(self,request):
        user = request.user
        coding  = list(Skillset.objects.filter(user=user).values('coding'))[-1]
        leadership  = list(Skillset.objects.filter(user=user).values('leadership'))[-1]
        communication  = list(Skillset.objects.filter(user=user).values('communication'))[-1]
        presentation  = list(Skillset.objects.filter(user=user).values('presentation'))[-1]

        context = {
            'user_id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'coding' : (coding['coding'] + 1)*16,
            'leadership' : (leadership['leadership']+1)*16,
            'communication' : (communication['communication']+1)*16,
            'presentation' : (presentation['presentation']+1)*16,
        }
        return render(request, 'student_profile.html', context)

    def post(self,request):
        pass

class Question_Form(View):
    def get(self,request,title):  # Assuming the form ID is passed in the URL
        random_questions = questionaries.create_random_question_dict()


        context = {
            'page_name':'question_form',
            'random_questions' : random_questions,
            'title' : title,
        }
        return render(request, "questionform.html", context)
    def post(self,request):
        if request.method == 'POST':
            user = request.user
            user_id = request.user.id
            email = request.user.email if request.user.email else request.user.username
            name = request.user.username

            title = request.POST.get('title')
            coding_question = request.POST.get('question_0')
            leadership_question = request.POST.get('question_1')
            communication_question = request.POST.get('question_2')  
            presentation_question = request.POST.get('question_3')  
            skillset = Skillset.objects.create(
                user = user,
                title = title,
                coding = coding_question,
                leadership = leadership_question,
                communication = communication_question,
                presentation = presentation_question,
            )
            if skillset:
                df = pd.DataFrame.from_dict([{
                    "user_id": user_id,
                    "name" : name,
                    "email" : email,
                    "coding": (int(skillset.coding) + 1)*16,
                    "leadership": (int(skillset.leadership) + 1)*16,
                    "communication": (int(skillset.communication) + 1)*16,
                    "presentation": (int(skillset.presentation) + 1)*16,
                }])
                name = "data/data.csv"
                df.to_csv(name, mode='a', header=not os.path.exists(name), index=False, lineterminator='\n')
                skillset.save()
        return redirect( "/")

class Team_Generator(View):
    def get(self,request):  # Assuming the form ID is passed in the URL
        return render(request, "activate.html")

