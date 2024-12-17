from datetime import date
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from HRadministrator.models import *
from candidate.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import auth, User
# Create your views here.

@login_required(login_url="/")
def candidate_home(request):
    user = request.user
    return render(request, 'home.html', {'user':user})

@login_required(login_url="/")
def candidate_dashboard(request):
    requi = requisition.objects.all().count
    post = position.objects.all().count
    context = {
        'requi':requi,
        'post':post,
    }
    return render(request, 'candidate_dashboard.html', context)

@login_required(login_url="/")
def candidate_profile(request):
    user = request.user
    print("USer id ",user.username)
    data=candidate.objects.filter(cand_id=user.username)
    return render(request, 'profile.html',{'data':data})


@login_required(login_url="/")
def candidate_openpositions(request):
    posts = position.objects.all()
    return render(request, 'pos.html', {'posts':posts})



@login_required(login_url="/")
def candidate_requisition(request):
    posts = requisition.objects.all()
    return render(request, 'requisition.html', {'posts':posts})



@login_required(login_url="/")
def candidate_cfeedback(request):
    return render(request, 'feedback.html')

@login_required(login_url="/")
def candidate_changepassword(request):
    return render(request, 'changepassword.html')

@login_required(login_url="/")
def candidate_changepasswordDB(request):
    user = request.user
    print("User id is ",user)
    password = request.POST.get('pwd')
    cnfpswd = request.POST.get('cpwd')
    if password == cnfpswd:
            pswd = make_password(password)
            User.objects.filter(username=user).update(password=pswd)

    return render(request, 'home.html', {'user':user})


@login_required(login_url="/")
def candidate_feedbackDB(request):
    user = request.user
    data=candidate.objects.filter(cand_id=user.username)
    cid=data[0].cand_id
    cname=data[0].first_name+" "+data[0].last_name
    feedback = request.GET.get('feedback')
    today = date.today()
    Feedback(canid=cid,cname=cname,feedback=feedback,feedbackdt=today).save()
    user = user.username
    return render(request, 'home.html', {'user':user})
        
