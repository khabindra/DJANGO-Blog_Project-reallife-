from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BlogCategory,BlogPost
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    if request.user.is_authenticated:

        categories = BlogCategory.objects.all()
        fnews = BlogPost.objects.all()
        context = {
            'categories':categories,
            'fnews':fnews,
        }
        return render(request,'index.html',context)
    else:
        return redirect('login_form')
def send_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = 'Python Training at Sipalaya'
            # message = 'This is a test email from Django'
        message = render_to_string('test.html')
        from_email = 'pujakhabi78@gmail.com'
        recipient_list = ['khabindratamang7@gmail.com',email]
        send_mail(subject, message, from_email, recipient_list,fail_silently=False,html_message=message)
        return HttpResponse('successfull !!!')
    
def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_form')
    else:
        form = UserCreationForm()

    return render(request, 'register.html',{'form':form})
# registration username: sipalaya 
# registration password: password123@
def login_form(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password  = request.POST['password']
        user = authenticate(request,username = uname, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login_form')
    return render(request,'login.html' )
def logout_form(request):
    logout(request)
    return redirect('login_form')