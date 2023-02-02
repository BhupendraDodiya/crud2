from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from app.models import Emp
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method=="POST":
        na = request.POST['n']
        do = request.POST['d']
        co = request.POST['c']
        em = request.POST['e']
        pa = make_password(request.POST['p'])
        if Emp.objects.filter(Email=em).exists():
            messages.error(request,'email already exist')
            return redirect('/')
        elif Emp.objects.filter(Contact=co).exists():
            messages.error(request,'contact already exist')
            return redirect('/')
        else:
            Emp.objects.create(Name=na,Dob=do,Contact=co,Email=em,Password=pa)
            return HttpResponse('created succesfuly')

def login(request):
    return render(request,'login.html')

def log_detail(request):
    if request.method=='POST':
        ema = request.POST['e']
        pas = request.POST['p']
        if Emp.objects.filter(Email=ema).exists():
            obj = Emp.objects.get(Email=ema)
            psw = obj.Password
            if check_password(pas, psw):
                return HttpResponse('welcome')
            else:
                messages.error(request,'Password incorrect')
                return redirect('/login/')
        else:
            messages.error(request,"Email Not Exist")
            return redirect('/login/')

def table(request):
    res=Emp.objects.all()
    return render(request,'table.html',{'tab':res})

def update(request,uid):
    res = Emp.objects.get(id=uid)
    return render(request,"update.html",{'da':res})

def update_form(request):
    if request.method=="POST":
        ui = request.POST['u']
        na = request.POST['n']
        do = request.POST['d']
        co = request.POST['c']
        em = request.POST['e']
        Emp.objects.filter(id=ui).update(Name=na,Dob=do,Contact=co,Email=em)
        return redirect('/table/')
        
def delete_form(request,pk):
    Emp.objects.filter(id=pk).delete()
    return redirect('/table/')