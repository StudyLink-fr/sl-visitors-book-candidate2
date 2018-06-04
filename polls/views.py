from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime

from .models import Notice, User

password = None

#home_page

def index(request):
    global password
    password = None
    all_notice = Notice.objects.order_by('-pub_date')
    context = {
        'all_notice': all_notice,
    }
    return render(request, 'polls/index.html', context)

#home_page connect

def index_log(request, pseudo):
    user = get_object_or_404(User, pseudo=pseudo)
    global password
    if password == "login":
        password = user.password
    if password != user.password:
        return HttpResponseRedirect(reverse('polls:index'))
    all_notice = Notice.objects.order_by('-pub_date')
    context = {
        'all_notice': all_notice,
        'pseudo': pseudo,
    }
    return render(request, 'polls/index_log.html', context)

#add a new notice when connected

def send(request, pseudo):
    if request.POST['title'] == "" or request.POST['text'] == "":
        return HttpResponseRedirect(reverse('polls:index_log', args=(), kwargs={'pseudo': pseudo}))
    notice = Notice(
        notice_title=request.POST['title'],
        notice_text=request.POST['text'],
        post_pseudo=pseudo,
        pub_date=datetime.now()
    )
    notice.save()
    return HttpResponseRedirect(reverse('polls:index_log', args=(), kwargs={'pseudo': pseudo}))

#delete a notice when connected

def delete(request, pseudo, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    notice.delete()
    return HttpResponseRedirect(reverse('polls:index_log', args=(), kwargs={'pseudo': pseudo}))

#modify a notice when connected

def change_notice(request, pseudo, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    if notice.post_pseudo != pseudo:
        return HttpResponseRedirect(reverse('polls:index_log', args=(), kwargs={'pseudo': pseudo}))
    context = {
        'pseudo': pseudo,
        'notice': notice,
    }
    return render(request, 'polls/change_notice.html', context)

#modify in database

def change_now(request, pseudo, notice_id):
    if request.POST['title'] == "" or request.POST['text'] == "":
        return HttpResponseRedirect(reverse('polls:change_notice', args=(), kwargs={'pseudo': pseudo, 'notice_id': notice_id}))
    notice = get_object_or_404(Notice, pk=notice_id)
    notice.notice_title = request.POST['title']
    notice.notice_text = request.POST['text']
    notice.save()
    return HttpResponseRedirect(reverse('polls:index_log', args=(), kwargs={'pseudo': pseudo}))

#register an account

def register(request):
    return render(request, 'polls/register.html')

#set new account in database

def register_try(request):
    if request.POST['pseudo'] == "" or request.POST['password'] == "" or request.POST['password'] != request.POST['confirm_password']:
        return HttpResponseRedirect(reverse('polls:register'))
    user = User(
        pseudo=request.POST['pseudo'],
        password=request.POST['password'],
    )
    user.save()
    return HttpResponseRedirect(reverse('polls:register'))

#login an account

def login(request):
    return render(request, 'polls/login.html')

#check account to login

def login_try(request):
    if request.POST['pseudo'] == "" or request.POST['password'] == "":
        return HttpResponseRedirect(reverse('polls:login'))
    all_user = User.objects.order_by('id')
    num_page = 1
    for user in all_user:
        if request.POST['pseudo'] == user.pseudo and request.POST['password'] == user.password:
            global password
            password = "login"
            return HttpResponseRedirect(reverse('polls:index_log', args=(), kwargs={'pseudo': user.pseudo}))
    return render(request, 'polls/login.html')
