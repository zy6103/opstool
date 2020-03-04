from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout,login
from remote_manager import models
import json
# Create your views here.

def acc_login(request):
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('/')
        else:
            error_msg = 'Wrong username or password'

    return render(request,'login.html',{'error_msg':error_msg})

def acc_logout(request):
    logout(request)
    return redirect('/login')

@login_required
def dashboard(request):
    return render(request, 'index.html')

@login_required
def auto_check(request):

    return render(request,'remote_manager/auto_check.html')

@login_required
def start_check(request):
    if request.method == 'POST':
        task_data = json.loads(request.POST.get('task_data'))
        host_obj = []  # {'ip': '192.168.56.134', 'port': 22, 'logname': 'root', 'logpwd': 'ls3du8', 'type': 'redhat7'}
        for id in task_data:
            tmp = {}
            host_tmp = models.HostTab.objects.get(id=id)
            tmp['ip'] = host_tmp.ip_addr
            tmp['port'] = host_tmp.port
            tmp['logname'] = host_tmp.login_user
            tmp['logpwd'] = host_tmp.login_pwd
            tmp['type'] = host_tmp.sys_type_tab.name
            host_obj.append(tmp)

        return HttpResponse('ok')