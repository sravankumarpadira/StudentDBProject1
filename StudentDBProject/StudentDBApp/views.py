from django.shortcuts import render
from StudentDBApp.forms import StudentLoginForm
from StudentDBApp.forms import SignupForm

def studentloginpageviews(request):
    formObj=StudentLoginForm();
    dict1={'form1': formObj}
    return  render(request,'StudentDBApp/login.html', context=dict1);

def signup_form_views(request):
    sentdata=False;
    formObj=SignupForm();
    if request.method=='post':
        formObj=SignupForm(request.post)
        print('basic validation compelete and printing data')
        print('Name:',formObj.cleaned_data['name'])
        print('Password:',formObj.cleaned_data['password'])
        print('Email:',formObj.cleaned_data['email'])
        formObj= SignupForm();
        sentdata=True;
    return render(request,'StudentDBApp/signup.html',{'Form1':formObj,'Sentdata':sentdata})
