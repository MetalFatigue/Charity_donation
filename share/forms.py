from django import forms
from share.models import User, Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'
        exclude = ('user', )
#
# //TODO: validacja //