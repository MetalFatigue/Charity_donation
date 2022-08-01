from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from accounts.models import User
from share.models import Donation, Institution


class LandingPage(View):
    def get(self, request):
        bags = Donation.objects.all().aggregate(Sum('quantity'))
        institutions = Institution.objects.all()
        foundations = institutions.filter(type=0)
        non_government_organization = institutions.filter(type=1)
        community_collection = institutions.filter(type=2)
        donated_institutions = institutions.filter(donation__quantity__gt=0).count()
        if request.user.is_authenticated:
            name = request.user.first_name
        else:
            name = ''

        context = {
            "bags": bags,
            "foundations": foundations,
            "non_government_organization": non_government_organization,
            "community_collection": community_collection,
            "donated_institution": donated_institutions,
            "name": name
        }
        return render(request, "index.html", context)


class AddDonation(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "form.html")


class UserProfil(View):
    def get(self, request):
        user = User.objects.get(email=request.user.email)
        bags = Donation.objects.filter(user=user).aggregate(Sum('quantity'))
        institutions = Institution.objects.filter(donation__user=user)
        foundations = institutions.filter(type=0)
        non_government_organization = institutions.filter(type=1)
        community_collection = institutions.filter(type=2)
        donations = Donation.objects.filter(user=user)
        context = {
            "donations": donations,
            "user": user,
            "bags": bags,
            "foundations": foundations,
            "non_government_organization": non_government_organization,
            "community_collection": community_collection,
        }
        return render(request, "user-profil.html", context)
