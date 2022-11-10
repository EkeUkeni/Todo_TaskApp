from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        # username = request.POST['username']
        # password = request.POST['password1']
        if form.is_valid():
            form.save()
            # user = authenticate(request, username=username, password=password)
            # if user is not None:
            #     login(request, user)

            return redirect("account:login")
            # return redirect("taskapp:home")

    
    context = {
        "form":form
    }

    return render(request, "account/register.html", context)

def login_view(request):
    form = AuthenticationForm()

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect("taskapp:home")
        else:
            messages.error(request, "Username or Password is incorrect!")

    context = {
        'form':form
    }

    return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)

    return redirect('account:login')
