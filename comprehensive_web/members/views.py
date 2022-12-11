from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Member

import hashlib
# Create your views here.
def login(request):
    msg = ""
    if "account" in request.POST and "pwd" in request.POST:
        account = request.POST['account']
        password = request.POST['pwd']
        
        # password = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
        password = hashlib.sha3_256(password.encode(encoding='utf-8')).hexdigest()
        
        obj = Member.objects.filter(email = account,
                                    password = password).count()
        
        if obj > 0:
            request.session['account'] = account
            request.session['isAlive'] = True
            
            return HttpResponseRedirect('/all_cartoon')
            
        
        else:
            msg = "帳密錯誤請重新輸入"
            return render(request, 'login.html', locals())
            # return HttpResponseRedirect('/all_cartoon')
        
    
    else:
        if "account" in request.session and "isAlive" in request.session:
            return HttpResponseRedirect("/cartoon")
        
        else:
            msg = "歡迎光臨"
            return render(request, 'login.html', locals())
    # return render(request, 'login.html')

def logout(request):
    pass

def register(request):
    msg = ""
    
    if "account" in request.POST:
        account = request.POST['account']
        username = request.POST['username']
        password = request.POST['pwd']
        birthday = request.POST['birthday']
        sex = request.POST['sex']
        
        password = hashlib.sha3_256(password.encode(encoding='utf-8')).hexdigest()
        
        obj = Member.objects.filter(email = account).count()
        
        if obj == 0:
            member = Member.objects.create(email = account,
                                           username = username,
                                           password = password,
                                           birthday = birthday,
                                           sex = sex)
            
            member.save()
            msg = "註冊完成"
            
            return HttpResponseRedirect('/login')
        else:
            msg="Email已註冊"
    
    return render(request, 'register.html', locals())

def member_manage(request):
    pass