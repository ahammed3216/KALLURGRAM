from django.contrib.auth import authenticate,logout
from .models import Profile
from django.shortcuts import redirect, render
from .forms import ProfileForm,LoginForm, RegisterForm, User
# Create your views here.


def profileView(request):
    form=ProfileForm(request.POST ,request.FILES)
    profile=Profile()
    if form.is_valid():
        print("hai")
        print(form.cleaned_data)
        first_name=form.cleaned_data.get('first_name')
        second_name=form.cleaned_data.get('second_name')
        address=form.cleaned_data.get('address')
        phone_no=form.cleaned_data.get('phonenumber')
        ward=form.cleaned_data.get('ward')
        panchayath=form.cleaned_data.get('panchayath')
        email=form.cleaned_data.get('email')
        house_no=form.cleaned_data.get('house_no')
        image=form.cleaned_data.get('image')


      
        profile.first_name=first_name
        profile.second_name=second_name
        profile.address=address
        profile.phonenumber=phone_no
        profile.ward=ward
        profile.panchayath=panchayath
        profile.email=email
        profile.house_no=house_no
        profile.image=image
        profile.user=request.user
        profile.save()

        return redirect('/')
       
    print(form.errors)
    context={
        'form':form,
    }
    return render(request,"profileform.html",context)




def home(request):
    return render(request,"home_page.html")


def Register(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password1=form.cleaned_data.get('password1')
        password2=form.cleaned_data.get('password2')

        user=User.objects.create_user(username,email,password2)

        user.save()

        return redirect('/')
    

    return render(request,'register.html',context={'form':form})


def LoginView(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        
        
        authenticate(username=username,password=password)
        user=User.objects.get(username=username)
        email=user.email
        
        print(email)

        return redirect('/')

    return render (request,"login.html",context={'form':form})



def logoutview(request):
    
    logout(request)
    print("h")
    return redirect('/')
