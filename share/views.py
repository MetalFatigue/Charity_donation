from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from accounts.models import User
from share.forms import DonationForm
from share.models import Donation, Institution, Category


class LandingPage(View):
    def get(self, request):
        quantity = Donation.objects.all().aggregate(Sum('quantity'))
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
            "quantity": quantity,
            "foundations": foundations,
            "non_government_organization": non_government_organization,
            "community_collection": community_collection,
            "donated_institution": donated_institutions,
            "name": name
        }
        return render(request, "index.html", context)


class AddDonation(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "form.html", {"categories": categories})

    def post(self, request):
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user
            donation.save()
            donation.categories.set(form.cleaned_data.get('categories'))
            donation.save()
            return render(request, 'form-confirmation.html')

        return render(request, 'form-fail.html')

def get_institution_by_category(request):
    categories_ids = request.GET.getlist('id')
    institutions = Institution.objects.all()
    for category_id in categories_ids:
        institutions = institutions.filter(categories__id=category_id)
    data = serialize('json', institutions)
    return HttpResponse(data, content_type="application/json")


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

    def post(self, request):
        donation_id = request.POST.get('id')
        donation = Donation.objects.get(id=donation_id)
        donation.is_taken = True
        donation.save()
        return redirect('profil')


def donation_taken(request):
        donation_id = request.GET.get('id')
        print(donation_id)
        donation = Donation.objects.filter(id=donation_id)
        donation.is_taken = True
        donation.update()

        data = serialize('json', donation)
        return HttpResponse(data, content_type="application/json")
