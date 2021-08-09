from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
# Create your views here.


class LoginView(View):
    template_name = 'user/login.html'

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        context = {'authentication_form': form}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("login incorrect")
        else:
            return HttpResponse("form incorrect")


def homepage(request):
    return render(request=request, template_name="main/head.html")


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("user:homepage")
