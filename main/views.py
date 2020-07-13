from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.models import User

from .models import email_subscribe,course,course_level,popular_course,transaction_table,contact_message
from .forms import contact_form,transaction_form
# Create your views here.

class course_applied(View):
    def get(self, request, user_id):
        items = transaction_table.objects.filter(user_id=user_id)
        datas = list()
        for item in items:
            course_id = item.course_id
            course_title = course.objects.get(id=course_id).title
            datas.append({
                'course_title': course_title
            })
        return render(request, 'profile-course-applied.html', {
            'datas': datas
        })

class my_course(View):
    def get(self, request, user_id):
        items = transaction_table.objects.filter(user_id=user_id, verified=True)
        datas = list()
        for item in items:
            course_id = item.course_id
            course_title = course.objects.get(id=course_id).title
            datas.append({
                'course_title': course_title
            })
        return render(request, 'profile-my-course.html', {
            'datas': datas
        })

class my_transaction(View):
    def get(self, request, user_id):
        items = transaction_table.objects.filter(user_id=user_id)
        datas = list()
        for item in items:
            t_id = item.t_id
            datas.append({
                't_id': t_id
            })
        return render(request, 'profile-my-transaction.html', {
            'datas': datas
        })

class home(View):
    def get(self, request):
        items = popular_course.objects.all()
        datas = list()
        for item in items:
            course_id = item.course_id
            course_title = course.objects.get(id=course_id).title
            level_id = course.objects.get(id=course_id).level_id
            c_level = course_level.objects.get(id=level_id).title
            course_duration = course.objects.get(id=course_id).duration
            course_desc = course.objects.get(id=course_id).description
            datas.append({
                'course_id': course_id,
                'course_title': course_title,
                'course_level': c_level,
                'course_duration': course_duration,
                'course_desc': course_desc
            })
        return render(request, 'index.html', {
            'datas': datas
        })

class login(View):
    def get(self, request):
        return render(request, 'login.html')

class logout_request(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class courses(View):
    def get(self, request):
        items = course.objects.all()
        datas = list()
        for item in items:
            course_id = item.id
            course_title = item.title
            level_id = item.level_id
            c_level = course_level.objects.get(id=level_id).title
            course_duration = item.duration
            course_desc = item.description
            datas.append({
                'course_id': course_id,
                'course_title': course_title,
                'course_level': c_level,
                'course_duration': course_duration,
                'course_desc': course_desc
            })
        return render(request, 'course.html', {
            'datas': datas
        })

class profile(View):
    def get(self, request, user_id):
        username = User.objects.get(id=user_id).username
        course_applied = transaction_table.objects.filter(user_id=user_id).count()
        verified_transaction = transaction_table.objects.filter(user_id=user_id, verified=True).count()
        datas = {
            'username': username,
            'course_applied': course_applied,
            'verified_transaction': verified_transaction
        }
        return render(request, 'profile.html', {
            'datas': datas
        })

class contact(View):
    def get(self, request):
        form = contact_form()
        return render(request, 'contact.html', {
            'form': form
        })
    
    def post(self, request):
        form = contact_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            subject = form['subject']
            user_id = request.user.id
            try:
                data = contact_message.objects.get(user_id=user_id, subject=subject)
                pass
            except:
                data = contact_message()
                data.user_id = user_id
                data.subject = subject
                data.save()
        return redirect('/')

class subscribe(View):
    def post(self, request):
        email = request.POST.get('email')
        if email == '':
            pass
        else:
            data = email_subscribe()
            data.email = email
            data.save()
        return redirect('/')
    
class transaction(View):
    def get(self, request, course_id):
        item = course.objects.get(id=course_id)
        course_title = item.title
        level_id = item.level_id
        c_level = course_level.objects.get(id=level_id).title
        course_duration = item.duration
        datas = {
            'course_title': course_title,
            'course_level': c_level,
            'course_duration': course_duration
        }
        form = transaction_form()
        return render(request, 'transaction.html', {
            'datas': datas,
            'form': form
        })
    
    def post(self, request, course_id):
        form = transaction_form(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            t_id = form['t_id']
            user_id = request.user.id
            try:
                data = transaction_table.objects.get(user_id=user_id, t_id=t_id, course_id=course_id)
                pass
            except:
                data = transaction_table()
                data.t_id = t_id
                data.user_id = user_id
                data.course_id = course_id
                data.save()
        return render(request, 'submitted.html')