from django import forms
from django.forms import ModelForm
from django.forms.widgets import EmailInput,TextInput
from web.models import Contact
from web.models import COMPANY_SIZE,INDUSTRY,COUNTRY,JOB_ROLE


EMPTY_COMPANY_SIZE = (("","Company Size"),) + COMPANY_SIZE
EMPTY_INDUSTRY = (("","Industry"),) + INDUSTRY
EMPTY_JOB_ROLE = (("","Job Role"),) + JOB_ROLE
EMPTY_COUNTRY = (("","Country"),) + COUNTRY
class ContactForm(ModelForm):
    company_size = forms.ChoiceField(choices=EMPTY_COMPANY_SIZE)
    industry = forms.ChoiceField(choices=EMPTY_INDUSTRY)
    job_role = forms.ChoiceField(choices=EMPTY_JOB_ROLE)
    country = forms.ChoiceField(choices=EMPTY_COUNTRY)
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "email" : EmailInput(attrs={"placeholder":"Email"}),
            "first_name" : TextInput(attrs={"placeholder":"First Name"}),
            "last_name" : TextInput(attrs={"placeholder":"Last Name"}),
            "company" : TextInput(attrs={"placeholder":"Company"})
        }