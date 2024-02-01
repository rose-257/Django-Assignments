from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import student

# Create your views here.

def studentreg(request):
    form = StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,'register.html',{'form':form})

def read(request):
    cr=student.objects.all()
    return render(request,'read.html',{'cr':cr})

def update(request,pk):
    cr = student.objects.get(id=pk)
    form = StudentForm(instance= cr)
    if request.method=="POST":
        form = StudentForm(request.POST,instance=cr)
        if form.is_valid():
            form.save()
            return redirect('read')
    return render(request, "update.html",{'form':form})  

def delete(request,pk):
    cr=student.objects.get(id=pk)
    cr.delete()
    return redirect('read')

def login(request):
    form = StudentForm()
    return render(request,'login.html',{'form':form})
    
def welcome(request):
    firstname=request.session['firstname']
    return render(request,'welcome.html',{'firstname':firstname})


def userlog(request):
    if request.method=='POST':
        email= request.POST.get('email')
        password= request.POST.get('password')
        cr= student.objects.filter(email=email,password=password)
        form=StudentForm()
        if cr:
            #------------------added code for showing details in welome page----(day18)------
            user_details=student.objects.get(email=email,password=password)
            id=user_details.id
            firstname=user_details.firstname
            email=user_details.email
            password=user_details.password

            request.session['id']=id
            request.session['firstname']=firstname
    
            return redirect('welcome')
        else:
            ce="Invalid Username or Password"
            return render(request,'login.html',{'ce':ce,'form':form})
    else:
        return render(request,'register.html')  