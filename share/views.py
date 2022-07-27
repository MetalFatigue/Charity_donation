from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from share.models import Donation, Institution


class LandingPage(View):
    def get(self, request):
        bags = Donation.objects.all().aggregate(Sum('quantity'))
        institutions = Institution.objects.all()
        donated_institutions = institutions.filter(donation__quantity__gt=0).count()
        return render(request, "index.html", {"bags": bags, "institutions": institutions,
                                              "donated_institution": donated_institutions})


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class Login(View):
    def get(self, request):
        return render(request, "login.html")


class Register(View):
    def get(self, request):
        return render(request, "register.html")
