from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

# Create your views here.


def Home(request):
    contact = SaveContact.objects.all()
    if request.method=='GET':
        contact = SaveContact.objects.all()
        search_input = request.GET.get('search-area')
        if search_input:
            contact = SaveContact.objects.filter(full_name__icontains = search_input)
            
        else:
            contact = SaveContact.objects.all()
            search_input= ''
    return render(request,"Home.html",{'contact':contact,'search_input':search_input})


def token_send(request):
    return render(request,'token_send.html')

def userdetail(request):

    if request.method == "POST":
        firstname = request.POST['fname']
        midname = request.POST['mname']
        lastname = request.POST['lname']
        number = request.POST['phone']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        
        try:
            if password!=cpassword:
                    messages.success(request, ' Password and Confirm Password does not match.')
                    return redirect('/Signup')
                
            if User.objects.filter(username = username).first():
                    messages.success(request, ' Username is taken.')
                    return redirect('/Signup')
            if User.objects.filter(email = email).first():
                        messages.success(request, ' email is taken.')
                        return redirect('/Signup')

            

            user_obj = User.objects.create_user(username = username, email=email, password=password)
            user_obj.save()
            

            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user= user_obj, auth_token = auth_token)
            profile_obj.save()

            sent_mail(email, auth_token)
            
        except Exception as e:
            print(e)

        us = usersave(first=firstname, middle=midname, last=lastname, user=username, email=email, phoneno=number, password=password, cpassword=cpassword)
        us.save()
    return render(request,'token_send.html')

def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                 messages.success(request, 'Your account is already verified')
                 return redirect('/Login')

            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified')
            return redirect('/Login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)

def error(request):
    return render(request,'error.html')

def sent_mail(email,token):
    subject = 'Your account need to be verified.'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message, email_from, recipient_list)

def Logout(request):
    logout(request)
    return redirect('/')

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        request.session['username']=username
        password = request.POST['password']
        user_obj =  User.objects.filter(username=username).first()
    
        if user_obj is None:
            messages.success(request,'Wrong username')
            return redirect('/Login')

        profile_obj = Profile.objects.filter(user = user_obj).first()

        if not profile_obj.is_verified:
            messages.success(request,'Profile not verified.')
            return redirect('/Login')

        user = authenticate(request,username=username,password=password)
        if user is None:
            messages.success(request,'Wrong Password')
            return redirect('/Login')
        login(request, user)
        return redirect('/')
   

    else:
        return render(request,'Login.html')
    
    
    
def About(request):

    return render(request,'About.html')   

def contact(request):

    return render(request,'Contact.html')

def contact_us(request):
    if request.method == 'POST':
        client_name = request.POST['client_name']
        client_email = request.POST['client_email']
        subject = request.POST ['subject']
        client_message = request.POST['client_message']

        contact = Contact(client_name=client_name, 
        client_email=client_email, subject=subject, client_message=client_message,)

        contact.save()
        messages.success(request,'Email sent successfully.')
        # Send client_email
        send_mail(
            'Inquiry',
            'There has been Inquiry for   ' + client_name +'.  From Email: ' + client_email + '.  Subject: ' + subject + '. Message:' + client_message + '.  Sign into the admin panel for more',
            'meetcboghani02@gmail.com',
            ['meetcboghani02@gmail.com'],
            fail_silently=False
        )

        return redirect('/contact')

def profile(request):
    prof = usersave.objects.all()

    return render(request,'UserProfile.html',{'prof':prof})

def uprofile(request):
    if request.method == "POST":
        firstname = request.POST['fname']
        midname = request.POST['mname']
        lastname = request.POST['lname']
        number = request.POST['phone']
        username = request.POST['username']
        id = usersave.objects.only('id').get(user=username).id
        
        usersave.objects.filter(id = id).update(first=firstname, middle=midname, last=lastname,phoneno=number)
    

        prof = usersave.objects.all()

    return render(request,'UserProfile.html',{'prof':prof})
    
def forgot(request):
    
    return render(request,'fpassword.html')

use = None
def fpassword(request):

    if request.method == 'POST':
        
        user1 = request.POST.get('user1')
         
        request.session['username']=user1   
         
        if User.objects.filter(username = user1).first():
                email = User.objects.only('email').get(username=user1).email
                subject = 'Forgot Password of the Account.'
                message = f'Hi paste the link to change password of your account http://127.0.0.1:8000/forpassword'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject,message, email_from, recipient_list)
                messages.success(request,"We've emailed you instructions for setting your password.")
            
        else: 
            messages.success(request,'Wrong email address')
      
    return render(request,'fPassword.html',{'user1':user1})

def forpassword(request):

    return render(request,'forpassword.html')

def pass1(request):
    
    if request.method == 'POST':
        
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        user1 = request.session['username']
        
        id = usersave.objects.only('id').get(user=user1).id
        user_obj = User.objects.only('id').get(username=user1)
        if password!=cpassword:
            messages.success(request, ' Password and Confirm Password does not match.')
            return redirect('/forpassword')
            
        if User.objects.filter(username = user1).first():
                        user_obj.set_password(password)
                        user_obj.save()
                        usersave.objects.filter(id=id).update(password=password,cpassword=cpassword)

        else:
                    return render(request,'/pass1')
        
       
    return redirect('/Login')

def addContact(request):
    
    if request.method == 'POST':

        new_contact = SaveContact(
            full_name=request.POST['fullname'],
            email=request.POST['email'],
            phone_number=request.POST['phonenumber'],
            address=request.POST['address'],
            user_name = request.POST['username']
            )
        new_contact.save()
        return redirect('/')

    return render(request, 'new.html')

def editContact(request, pk):
    contact = SaveContact.objects.get(id=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.email = request.POST['email1']
        contact.phone_number = request.POST['phone-number']
        contact.address = request.POST['address']
        contact.save()

        return redirect('/contactprofile/'+str(contact.id))
    return render(request, 'edit.html', {'contact': contact})

def deleteContact(request, pk):
    contact = SaveContact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')

    return render(request, 'delete.html', {'contact': contact})

def contactProfile(request, pk):
    contact = SaveContact.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact':contact})
