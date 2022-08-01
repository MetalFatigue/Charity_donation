from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
from accounts.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login


class Register(SuccessMessageMixin, generic.CreateView):
    """Widok rejestracji użytkownika"""
    template_name = 'register.html'
    form_class = RegisterForm
    success_message = "Dodano użytkownika"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.set_password(form.cleaned_data['password'])
        self.object.save()
        return response


class Login(View):
    """Widok logowania użytkownika"""
    def get(self, request):
        form = LoginForm
        return render(request, "login.html", {"form": form})

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect('/')
        else:
            form = LoginForm
            message = f'Użytkownik o podanym adresie email: {email} nie istnieje'
            return render(request, 'login.html', {"form": form, "message": message})

