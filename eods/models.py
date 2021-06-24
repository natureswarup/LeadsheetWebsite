from django.db import models
from datetime import datetime
from users.models import Account

# Create your models here.


class Office(models.Model):
    name = models.CharField(max_length=200)
    user = models.ManyToManyField(Account)
    email = models.EmailField(
        max_length=500)
    was_notified = models.BooleanField(
        verbose_name="Was the office notified?", default=False)

    def __str__(self):
        return self.name


class Leadsheet(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    ###Input Fields###
    file_upload = models.FileField(upload_to='pdfs', max_length=100)
    date_added = models.DateField()
    note = models.CharField(max_length=500, default="Place note here...")
    cash = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    electronic_checks = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    cc_amex = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cc_discover = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    cc_mastercard = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    cc_visa = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pnc_deposit = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    checks = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    eft = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    care_credit = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    lending_club = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    orthobanc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    flips = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    web_cc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    greensky = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    text2pay = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    other = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    total_daily_collections = models.DecimalField(
        max_digits=15, decimal_places=2, default=0,)

    ###Deposited Fields###

    cash_deposited = models.BooleanField("Cash Deposited?", default=False)
    electronic_checks_deposited = models.BooleanField(
        "Electronic Checks Deposited?", default=False)
    cc_amex_deposited = models.BooleanField("Amex Deposited?", default=False)
    cc_discover_deposited = models.BooleanField(
        "Discover Deposited?", default=False)
    cc_mastercard_deposited = models.BooleanField(
        "Mastercard Deposited?", default=False)
    cc_visa_deposited = models.BooleanField("Visa Deposited?", default=False)
    pnc_deposit_deposited = models.BooleanField(
        "PNC Deposited?", default=False)
    checks_deposited = models.BooleanField("Checks Deposited?", default=False)
    eft_deposited = models.BooleanField("EFT Deposited?", default=False)
    care_credit_deposited = models.BooleanField(
        "Carecredit Deposited?", default=False)
    lending_club_deposited = models.BooleanField(
        "Lending Club Deposited?", default=False)
    orthobanc_deposited = models.BooleanField(
        "OrthoBanc Deposited?", default=False)
    flips_deposited = models.BooleanField("Flips Deposited?", default=False)
    web_cc_deposited = models.BooleanField(
        "Web Credit Card Deposited?", default=False)
    greensky_deposited = models.BooleanField(
        "Greensky Deposited?", default=False)
    text2pay_deposited = models.BooleanField(
        "Text to Pay Deposited?", default=False)
    other_deposited = models.BooleanField(
        "Other Deposited?", default=False)

    ### Email ###
    email_sent = models.BooleanField(default=False)
    message = models.CharField(max_length=2000, default='Adjustment made...')

    def __str__(self):
        date = str(self.date_added)
        return date

    def total(self):
        total = self.cash + self.electronic_checks + self.cc_amex + self.cc_discover + self.cc_mastercard + self.cc_visa + self.pnc_deposit + self.checks + self.eft + \
            self.care_credit + self.lending_club + self.orthobanc + self.flips + \
            self.web_cc + self.greensky + self.text2pay + self.other
        return total

    def cashTotal(self):
        return self.cash

    def elecChkTotal(self):
        return self.electronic_checks

    def amexTotal(self):
        return self.cc_amex

    def discoverTotal(self):
        return self.cc_discover

    def mastercardTotal(self):
        return self.cc_mastercard

    def visaTotal(self):
        return self.cc_visa

    def pncTotal(self):
        return self.pnc_deposit

    def checksTotal(self):
        return self.checks

    def eftTotal(self):
        return self.eft

    def careCreditTotal(self):
        return self.care_credit

    def lendClubTotal(self):
        return self.lending_club

    def orthoTotal(self):
        return self.orthobanc

    def flipsTotal(self):
        return self.flips

    def webCCTotal(self):
        return self.web_cc

    def greenskyTotal(self):
        return self.greensky

    def t2pTotal(self):
        return self.text2pay

    def otherTotal(self):
        return self.other
