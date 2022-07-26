from django.shortcuts import render
from django.views import View

from share.models import Donation, Institution


class LandingPage(View):
    def get(self, request):
        bags = Donation.objects.all().count() # trzeba mnożyć razy quantity zeby wyszły worki
        institution = Institution.objects.all().count() # tu maja buć te co dostały a nie wszystkie
        return render(request, "index.html", {"bags": bags, "institution": institution})


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")


class Register(View):
    def get(self, request):
        return render(request, "register.html")
