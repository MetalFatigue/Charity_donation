from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.forms import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
from share.models import Donation, Institution
# from share.forms import RegisterForm

class LandingPage(View):
    def get(self, request):
        bags = Donation.objects.all().aggregate(Sum('quantity'))
        institutions = Institution.objects.all()
        foundations = institutions.filter(type=0)
        non_government_organization = institutions.filter(type=1)
        community_collection = institutions.filter(type=2)
        donated_institutions = institutions.filter(donation__quantity__gt=0).count()
        context = {
            "bags": bags,
            "foundations": foundations,
            "non_government_organization": non_government_organization,
            "community_collection": community_collection,
            "donated_institution": donated_institutions
        }
        return render(request, "index.html", context)


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")


# class Register(SuccessMessageMixin, generic.CreateView):
#     """Widok rejestracji użytkownika"""
#     template_name = 'register.html'
#     form_class = RegisterForm
#     success_message = "Dodano użytkownika"
#     success_url = reverse_lazy('login')

class Register(View):
    def get(self, request):
        return render(request, "register.html")

