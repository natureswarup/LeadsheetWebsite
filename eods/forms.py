from django import forms
from django.forms.fields import DateField


from .models import Office, Leadsheet


class LeadsheetForm(forms.ModelForm):

    class Meta:
        model = Leadsheet

        exclude = [
            'office', 'email_sent', 'message'
        ]

        widgets = {'date_added': forms.DateInput(
            format='%m%d%Y'), 'note': forms.Textarea(attrs={'rows': 5, 'cols': 100}), 'cash': forms.NumberInput(attrs={'onchange': 'calc()'}), 'electronic_checks': forms.NumberInput(attrs={'onchange': 'calc()'}), 'cc_amex': forms.NumberInput(attrs={'onchange': 'calc()'}), 'cc_discover': forms.NumberInput(attrs={'onchange': 'calc()'}), 'cc_mastercard': forms.NumberInput(attrs={'onchange': 'calc()'}), 'cc_visa': forms.NumberInput(attrs={'onchange': 'calc()'}), 'pnc_deposit': forms.NumberInput(attrs={'onchange': 'calc()'}), 'checks': forms.NumberInput(attrs={'onchange': 'calc()'}), 'eft': forms.NumberInput(attrs={'onchange': 'calc()'}), 'care_credit': forms.NumberInput(attrs={'onchange': 'calc()'}), 'lending_club': forms.NumberInput(attrs={'onchange': 'calc()'}), 'orthobanc': forms.NumberInput(attrs={'onchange': 'calc()'}), 'flips': forms.NumberInput(attrs={'onchange': 'calc()'}), 'web_cc': forms.NumberInput(attrs={'onchange': 'calc()'}), 'greensky': forms.NumberInput(attrs={'onchange': 'calc()'}), 'text2pay': forms.NumberInput(attrs={'onchange': 'calc()'}), 'other': forms.NumberInput(attrs={'onchange': 'calc()'})}


class Dateform(forms.Form):

    start_date = forms.DateField(widget=forms.DateInput(
        attrs={'placeholder': 'MM/DD/YYYY'}))
    end_date = forms.DateField(widget=forms.DateInput(
        attrs={'placeholder': 'MM/DD/YYYY'}))



class ContactForm(forms.ModelForm):
    class Meta:
        model = Leadsheet

        fields = ['message']

        widgets = {'message': forms.Textarea}
