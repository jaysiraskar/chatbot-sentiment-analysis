from .forms import ChatbotUserForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


# def registerpage(request):
#     pass
#     # if request.method == 'POST':
#     #     print("Got post")
#     #     print(dict(request.POST.items()))
#     #     # the Post request is to register a new user
#     #     if('register' in request.POST):
#     #         form1 = UserCreationForm(data=request.POST)
#     #         form2 = ChatbotUserForm(request.POST)
#     #         print('#### Form 1 ####', form1)
#     #         print('#### Form 2 ####', form2)
#     #         print("Validity 1 ### ", form1.is_valid())
#     #         print("Validity 2 ### ", form2.is_valid())
#     #         # username = form1.cleaned_data['username']
#     #         # password = form1.cleaned_data['password1']
#     #         # print("Username and password are ->>>", username, password)
#     #         # obj1 = form1.save(commit=False)
#     #         # obj1.username = username
#     #         # obj1.password1 = password
#     #         # obj1.password2 = form1.cleaned_data['password2']
#     #         # print("Validity 2 ### ", obj1.is_valid())
#     #         if form1.is_valid():
#     #             print("Saving form1 .................", form1.save())
#     #             username = form1.cleaned_data['username']
#     #             password = form1.cleaned_data['password1']
#     #             print("Username and password are ->>>", username, password)
#     #             user = authenticate(username=username, password=password)
#     #             login(request, user)
#     #             form2 = ChatbotUserForm(request.POST)
#     #             if(form2.is_valid()):
#     #                 obj = form2.save(commit=False)
#     #                 obj.user = user
#     #                 obj.save()
#     #             else:
#     #                 print('form2 not valid')
#     #             return redirect('profile')
#     #         else:
#     #             return redirect('register')
#     #     # the Post request is to login existing user user
#     #     elif('login' in request.POST):
#     #         # form3 = AuthenticationForm(request.POST)
#     #         username = request.POST.get('username')
#     #         password = request.POST.get('password')
#     #         print(username, password)
#     #         user = authenticate(username=username, password=password)
#     #         if user is not None:
#     #             login(request, user)
#     #             return redirect('profile')
#     #         else:
#     #             print("User not found")
#     #             messages.info(request, 'Username OR password is incorrect')
#     #         # login(request, user)
#     #             return render(request,'')
#     #     else:
#     #         print("### unknown Post Request ###")
#     #         return redirect('login')
#     # # GET request send the forms
#     # else:
#     #     print("Got get")
#     #     form1 = UserCreationForm()
#     #     form2 = ChatbotUserForm()
#     #     form3 = AuthenticationForm()
#     #     print("#### form 3 ##", form3)
#     #     context = {'form1': form1, 'form2': form2, 'form3': form3}
#     #     return render(request, "register.html", context)
#     return render(request, 'register.html')


def loginPage(request):
    form1 = None
    form2 = None
    if request.method == 'POST':
        print("Got post")
        print(dict(request.POST.items()))
        # the Post request is to register a new user
        if('register' in request.POST):
            form1 = UserCreationForm(data=request.POST)
            form2 = ChatbotUserForm(request.POST)
            print('#### Form 1 ####', form1)
            print('#### Form 2 ####', form2)
            print("Validity 1 ### ", form1.is_valid())
            print("Validity 2 ### ", form2.is_valid())
            # username = form1.cleaned_data['username']
            # password = form1.cleaned_data['password1']
            # print("Username and password are ->>>", username, password)
            # obj1 = form1.save(commit=False)
            # obj1.username = username
            # obj1.password1 = password
            # obj1.password2 = form1.cleaned_data['password2']
            # print("Validity 2 ### ", obj1.is_valid())
            if (form1.is_valid() and form2.is_valid()):
                print("Saving form1 .................", form1.save())
                username = form1.cleaned_data['username']
                password = form1.cleaned_data['password1']
                print("Username and password are ->>>", username, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                form2 = ChatbotUserForm(request.POST)
                obj = form2.save(commit=False)
                obj.user = user
                obj.save()
                # messages.success(request, 'Account created successfully')
                return redirect('profile')
            else:
                return redirect('login')
        # the Post request is to login existing user user
        elif('login' in request.POST):
            # form3 = AuthenticationForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                print("User not found")
                # messages.info(request, 'Username OR password is incorrect')
            # login(request, user)
                return redirect('login')
        else:
            print("### unknown Post Request ###")
    # GET request send the forms
    else:
        print("Got get")
        form1 = UserCreationForm()
        form2 = ChatbotUserForm()
        form3 = AuthenticationForm()
        print("#### form 3 ##", form3)
        context = {'form1': form1, 'form2': form2, 'form3': form3}
        return render(request, "login.html", context)
    # print(form1)
    # print(form2)
    # if(form1 == None):
    #     form1 = UserCreationForm()
    # if(form2 == None):
    #     form2 = ChatbotUserForm()

    # context = {}
    # return render(request, "login.html", context)

# TODO create a chatpage


def chatPage(request):
    return render(request, "login.html")


@login_required(login_url='login')
def profilePage(request):
    context = {'userdata': [request]}
    return(render(request, "profile.html"))


def logoutPage(request):
    logout(request)
    return render(request, 'logout.html')


# def testpage(request):
#     pass
    # form is sent as POST request
    # form1 = None
    # form2 = None
    # if request.method == 'POST':
    #     # print("Got post")
    #     # print(dict(request.POST.items()))
    #     # the Post request is to register a new user
    #     if('register' in request.POST):
    #         form1 = UserCreationForm(request.POST)
    #         form2 = ChatbotUserForm(request.POST)
    #         print('#### Form 2 ####', form2)
    #         if form1.is_valid():
    #             print("Saving form1 .................", form1.save())
    #             username = form1.cleaned_data['username']
    #             password = form1.cleaned_data['password1']
    #             print("Username and password are ->>>", username, password)
    #             user = authenticate(username=username, password=password)
    #             login(request, user)
    #             form2 = ChatbotUserForm(request.POST)
    #             if(form2.is_valid()):
    #                 obj = form2.save(commit=False)
    #                 obj.user = user
    #                 obj.save()
    #             else:
    #                 print('form2 not valid')
    #             return redirect('profile')
    #     # the Post request is to login existing user user
    #     elif('login' in request.POST):
    #         form1 = UserCreationForm(request.POST)
    #         username = request.POST.get('username')
    #         password = request.POST.get('password1')
    #         print(username, password)
    #         user = authenticate(username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect('profile')
    #         else:
    #             print("User not found")
    #             # messages.info(request, 'Username OR password is incorrect')
    #         # login(request, user)
    #         # return redirect('profile')
    #     else:
    #         print("### unknown Post Request ###")
    # # GET request send the forms
    # else:
    #     print("Got get")
    #     form1 = UserCreationForm()
    #     form2 = ChatbotUserForm()
    # # print(form1)
    # # print(form2)
    # if(form1 == None):
    #     form1 = UserCreationForm()
    # if(form2 == None):
    #     form2 = ChatbotUserForm()
    # context = {'form1': form1, 'form2': form2}

    # # context = {}
    # return render(request, "test.html", context)


# Test
# Test@123
# Test@gmail.com


# TestUser2
# Test2@999
# TestUser@gmail.com
