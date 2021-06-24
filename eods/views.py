from django.shortcuts import render, redirect
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Office, Leadsheet
from .forms import LeadsheetForm, Dateform, ContactForm
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import F
from decimal import Decimal
import csv

# Global Variables
date = datetime.datetime.now()
previous_date = datetime.datetime.today() - datetime.timedelta(days=1)
hour_of_day = int(date.strftime("%H"))
yesterday = (datetime.datetime.today() -
             datetime.timedelta(days=1)).strftime('%Y-%m-%d')
two_days = (datetime.datetime.today() -
            datetime.timedelta(days=2)).strftime('%Y-%m-%d')
three_days = (datetime.datetime.today() -
              datetime.timedelta(days=3)).strftime('%Y-%m-%d')
four_days = (datetime.datetime.today() -
             datetime.timedelta(days=4)).strftime('%Y-%m-%d')
five_days = (datetime.datetime.today() -
             datetime.timedelta(days=5)).strftime('%Y-%m-%d')
six_days = (datetime.datetime.today() -
            datetime.timedelta(days=6)).strftime('%Y-%m-%d')
seven_days = (datetime.datetime.today() -
              datetime.timedelta(days=7)).strftime('%Y-%m-%d')
eight_days = (datetime.datetime.today() -
              datetime.timedelta(days=8)).strftime('%Y-%m-%d')
nine_days = (datetime.datetime.today() -
             datetime.timedelta(days=9)).strftime('%Y-%m-%d')
ten_days = (datetime.datetime.today() -
            datetime.timedelta(days=10)).strftime('%Y-%m-%d')


def index(request):
    date = datetime.datetime.now()
    offices = Office.objects.all().order_by('name')
    previous_date = datetime.datetime.today() - datetime.timedelta(days=1)
    hour_of_day = int(date.strftime("%H"))
    yesterday = (datetime.datetime.today() -
                 datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    two_days = (datetime.datetime.today() -
                datetime.timedelta(days=2)).strftime('%Y-%m-%d')
    three_days = (datetime.datetime.today() -
                  datetime.timedelta(days=3)).strftime('%Y-%m-%d')
    four_days = (datetime.datetime.today() -
                 datetime.timedelta(days=4)).strftime('%Y-%m-%d')
    five_days = (datetime.datetime.today() -
                 datetime.timedelta(days=5)).strftime('%Y-%m-%d')
    six_days = (datetime.datetime.today() -
                datetime.timedelta(days=6)).strftime('%Y-%m-%d')
    seven_days = (datetime.datetime.today() -
                  datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    eight_days = (datetime.datetime.today() -
                  datetime.timedelta(days=8)).strftime('%Y-%m-%d')
    nine_days = (datetime.datetime.today() -
                 datetime.timedelta(days=9)).strftime('%Y-%m-%d')
    ten_days = (datetime.datetime.today() -
                datetime.timedelta(days=10)).strftime('%Y-%m-%d')
    days = [yesterday, two_days, three_days, four_days, five_days,
            six_days, seven_days, eight_days, nine_days, ten_days]
    info_lst = []
    total_yesterday = 0
    total_two_days = 0
    total_three_days = 0
    total_four_days = 0
    total_five_days = 0
    total_six_days = 0
    total_seven_days = 0
    total_eight_days = 0
    total_nine_days = 0
    total_ten_days = 0
    leadsheet_date = previous_date.strftime('%m-%d-%Y')

    # Get totals for previous 10 days
    for office in offices:
        leadsheets = office.leadsheet_set.all()[:20]
        info = {}
        info['name'] = office
        for ls in leadsheets:
            if str(ls.date_added) == yesterday:
                info['yesterday'] = ls.total()
                total_yesterday += ls.total()
            if str(ls.date_added) == two_days:
                info['two_days'] = ls.total()
                total_two_days += ls.total()
            if str(ls.date_added) == three_days:
                info['three_days'] = ls.total()
                total_three_days += ls.total()
            if str(ls.date_added) == four_days:
                info['four_days'] = ls.total()
                total_four_days += ls.total()
            if str(ls.date_added) == five_days:
                info['five_days'] = ls.total()
                total_five_days += ls.total()
            if str(ls.date_added) == six_days:
                info['six_days'] = ls.total()
                total_six_days += ls.total()
            if str(ls.date_added) == seven_days:
                info['seven_days'] = ls.total()
                total_seven_days += ls.total()
            if str(ls.date_added) == eight_days:
                info['eight_days'] = ls.total()
                total_eight_days += ls.total()
            if str(ls.date_added) == nine_days:
                info['nine_days'] = ls.total()
                total_nine_days += ls.total()
            if str(ls.date_added) == ten_days:
                info['ten_days'] = ls.total()
                total_ten_days += ls.total()
        info_lst.append(info)


    # Send email notifications if leadsheet is not submitted
    if previous_date.strftime("%A") == 'Friday' or previous_date.strftime("%A") == 'Saturday' or previous_date.strftime("%A") == 'Sunday':
        pass
    else:
        if hour_of_day >= int('9'):
            receipients = []
            subject = f'Reminder: Please submit your leadsheet for {leadsheet_date} to accounting'
            message = 'Please log into the leadsheet website and submit your financials.'
            sender = 'capstone.leadsheets@gmail.com'
            for office in offices:
                if office.leadsheet_set.all().first():
                    if previous_date.strftime('%Y-%m-%d') <= office.leadsheet_set.all().last().date_added.strftime("%Y-%m-%d"):
                        continue
                    else:
                        if office.was_notified == True:
                            continue
                        else:
                            if office.email not in receipients:
                                receipients.append(office.email)
                            office.was_notified = True
                            office.save()
            if receipients != []:
                email = EmailMessage(
                    subject,
                    message,
                    sender,
                    [],
                    receipients
                )
                email.send(fail_silently=True)

    context = {'offices': offices, 'yesterday': yesterday, 'two_days': two_days,
               'three_days': three_days, 'four_days': four_days, 'five_days': five_days, 'days': days, 'info_lst': info_lst, 'total_yesterday': total_yesterday, 'total_two_days': total_two_days, 'total_three_days': total_three_days, 'total_four_days': total_four_days, 'total_five_days': total_five_days, 'total_six_days': total_six_days, 'total_seven_days': total_seven_days, 'total_eight_days': total_eight_days, 'total_nine_days': total_nine_days, 'total_ten_days': total_ten_days, 'date': date}

    return render(request, 'eods/index.html', context)


@login_required(login_url='/users/login/')
def option(request, office_id):
    office = Office.objects.get(pk=office_id)
    users = office.user.all()
    context = {'office': office}

    if request.user.is_admin:
        return render(request, 'eods/option.html', context)
    for user in users:
        if str(user) == str(request.user):
            return render(request, 'eods/option.html', context)

    return render(request, 'eods/access.html')


@login_required
def create_lead(request, office_id):
    # Create Leadsheet form to submit
    date = datetime.datetime.now()
    office = Office.objects.get(pk=office_id)
    
    if request.method != 'POST':
        form = LeadsheetForm(initial={'date_added': date.strftime('%m/%d/%Y')})
    else:
        form = LeadsheetForm(request.POST, request.FILES)
        if form.is_valid():
            office.was_notified = False
            new_form = form.save(commit=False)
            new_form.office = office
            new_form.save()
            office.save()
            context = {'office': office, 'form': form}
            return render(request, 'eods/review_lead.html', context)
    context = {'office': office, 'form': form}
    return render(request, 'eods/create_lead.html', context)


@login_required
def view_lead(request, office_id):
    office = Office.objects.get(pk=office_id)
    leadsheets = office.leadsheet_set.order_by('-date_added')[:50]
    Office_Leadsheet = Leadsheet.objects.filter(office=office)
    total = 0
    cash = 0
    elecChk = 0
    amex = 0
    discover = 0
    mastercard = 0
    visa = 0
    webcc = 0
    pnc = 0
    checks = 0
    eft = 0
    carecredit = 0
    lending = 0
    ortho = 0
    flips = 0
    greensky = 0
    t2p = 0
    other = 0

    # Total leadsheets without any date filters
    for leadsheet in leadsheets:
        total += leadsheet.total()
        cash += leadsheet.cashTotal()
        elecChk += leadsheet.elecChkTotal()
        amex += leadsheet.amexTotal()
        discover += leadsheet.discoverTotal()
        mastercard += leadsheet.mastercardTotal()
        visa += leadsheet.visaTotal()
        webcc += leadsheet.webCCTotal()
        pnc += leadsheet.pncTotal()
        checks += leadsheet.checksTotal()
        eft += leadsheet.eftTotal()
        carecredit += leadsheet.careCreditTotal()
        lending += leadsheet.lendClubTotal()
        ortho += leadsheet.orthoTotal()
        flips += leadsheet.flipsTotal()
        greensky += leadsheet.greenskyTotal()
        t2p += leadsheet.t2pTotal()
        other += leadsheet.otherTotal()

    if request.method != 'POST':
        form1 = Dateform()

    else:
        form1 = Dateform(request.POST)

        if form1.is_valid():
            first = form1.cleaned_data['start_date']
            second = form1.cleaned_data['end_date']
            leadsheets = office.leadsheet_set.filter(
                date_added__range=(first, second)).order_by('-date_added')

            total = 0
            cash = 0
            elecChk = 0
            amex = 0
            discover = 0
            mastercard = 0
            visa = 0
            webcc = 0
            pnc = 0
            checks = 0
            eft = 0
            carecredit = 0
            lending = 0
            ortho = 0
            flips = 0
            greensky = 0
            t2p = 0
            other = 0

            # total leadsheets with date filters
            for leadsheet in leadsheets:
                total += leadsheet.total()
                cash += leadsheet.cashTotal()
                elecChk += leadsheet.elecChkTotal()
                amex += leadsheet.amexTotal()
                discover += leadsheet.discoverTotal()
                mastercard += leadsheet.mastercardTotal()
                visa += leadsheet.visaTotal()
                webcc += leadsheet.webCCTotal()
                pnc += leadsheet.pncTotal()
                checks += leadsheet.checksTotal()
                eft += leadsheet.eftTotal()
                carecredit += leadsheet.careCreditTotal()
                lending += leadsheet.lendClubTotal()
                ortho += leadsheet.orthoTotal()
                flips += leadsheet.flipsTotal()
                greensky += leadsheet.greenskyTotal()
                t2p += leadsheet.t2pTotal()
                other += leadsheet.otherTotal()

            context = {'office': office,
                       'leadsheets': leadsheets, 'form1': form1, 'total': total, 'cash': cash, 'elecChk': elecChk, 'amex': amex, 'discover': discover, 'mastercard': mastercard, 'visa': visa, 'webcc': webcc, 'pnc': pnc, 'checks': checks, 'eft': eft, 'carecredit': carecredit, 'lending': lending, 'ortho': ortho, 'flips': flips, 'greensky': greensky, 't2p': t2p, 'other': other}
            return render(request, 'eods/view_lead.html', context)

    context = {'office': office, 'leadsheets': leadsheets,
               'form1': form1, 'total': total, 'cash': cash, 'elecChk': elecChk, 'amex': amex, 'discover': discover, 'mastercard': mastercard, 'visa': visa, 'webcc': webcc, 'pnc': pnc, 'checks': checks, 'eft': eft, 'carecredit': carecredit, 'lending': lending, 'ortho': ortho, 'flips': flips, 'greensky': greensky, 't2p': t2p, 'other': other}
    return render(request, 'eods/view_lead.html', context)


@login_required
def edit_lead(request, office_id, leadsheet_id):
    leadsheet = Leadsheet.objects.get(id=leadsheet_id)
    office = leadsheet.office

    if request.method != 'POST':
        form = LeadsheetForm(instance=leadsheet, initial={
            'date_added': leadsheet.date_added.strftime('%m/%d/%Y')})
    else:
        form = LeadsheetForm(instance=leadsheet, data=request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('eods:view_lead', args=[office.id]))
    context = {'leadsheet': leadsheet, 'office': office,
               'form': form, 'leadsheet': leadsheet}
    return render(request, 'eods/edit_lead.html', context)


@login_required
def email_lead(request, office_id, leadsheet_id):
    leadsheet = Leadsheet.objects.get(id=leadsheet_id)
    office = leadsheet.office
    if request.method != 'POST':
        email_form = ContactForm(instance=leadsheet)
    else:
        email_form = ContactForm(data=request.POST, instance=leadsheet)

    if email_form.is_valid():
        leadsheet.email_sent = True
        # sent_from = email_form.cleaned_data['sent_from']
        message = email_form['message'].value()
        email = EmailMessage(subject='LEADSHEET ADJUSTMENT MADE - DO NOT REPLY TO THIS EMAIL',
                             body=message, from_email='capstone.leadsheets@gmail.com', to=(office.email,))
        email_form.save()
        email.send(fail_silently=False)

        return HttpResponseRedirect(reverse('eods:edit_lead', args=[office.id, leadsheet_id]))
    context = {'email_form': email_form}
    return render(request, 'eods/email_lead.html', context)


@login_required
def delete_lead(request, office_id, leadsheet_id):
    leadsheet = Leadsheet.objects.get(id=leadsheet_id)
    office = leadsheet.office
    delete = leadsheet.delete()
    return HttpResponseRedirect(reverse('eods:view_lead', args=[office.id]))



@login_required
def review_lead(request, office_id):
###Get the last leadsheet created ####
    office = Office.objects.get(pk=office_id)
    leadsheet = office.leadsheet_set.all().last()

    if request.method != 'POST':
        form = LeadsheetForm(instance=leadsheet, initial={
            'date_added': leadsheet.date_added.strftime('%m/%d/%Y')})
    else:
        form = LeadsheetForm(instance=leadsheet, data=request.POST)
        cash = form['cash'].value()
        elec_chk = form['electronic_checks'].value()
        pnc = form['pnc_deposit'].value()
        check = form['checks'].value()
        amex = form['cc_amex'].value()
        discover = form['cc_discover'].value()
        mc = form['cc_mastercard'].value()
        visa = form['cc_visa'].value()
        webcc = form['web_cc'].value()
        eft = form['eft'].value()
        carecredit = form['care_credit'].value()
        lendClub = form['lending_club'].value()
        ortho = form['orthobanc'].value()
        flips = form['flips'].value()
        greensky = form['greensky'].value()
        t2p = form['text2pay'].value()
        other = form['other'].value()

    if form.is_valid():
        if cash == '0':
            leadsheet.cash_deposited = True
        if elec_chk == '0':
            leadsheet.electronic_checks_deposited = True
        if pnc == '0':
            leadsheet.pnc_deposit_deposited = True
        if check == '0':
            leadsheet.checks_deposited = True
        if amex == '0':
            leadsheet.cc_amex_deposited = True
        if discover == '0':
            leadsheet.cc_discover_deposited = True
        if mc == '0':
            leadsheet.cc_mastercard_deposited = True
        if visa == '0':
            leadsheet.cc_visa_deposited = True
        if webcc == '0':
            leadsheet.web_cc_deposited = True
        if eft == '0':
            leadsheet.eft_deposited = True
        if carecredit == '0':
            leadsheet.care_credit_deposited = True
        if lendClub == '0':
            leadsheet.lending_club_deposited = True
        if ortho == '0':
            leadsheet.orthobanc_deposited = True
        if flips == '0':
            leadsheet.flips_deposited = True
        if greensky == '0':
            leadsheet.greensky_deposited = True
        if t2p == '0':
            leadsheet.text2pay_deposited = True
        if other == '0':
            leadsheet.other_deposited = True

        form.save()
        return HttpResponseRedirect(reverse('eods:option', args=[office.id]))
    context = {'leadsheet': leadsheet, 'office': office,
               'form': form, 'leadsheet': leadsheet}
    return render(request, 'eods/review_lead.html', context)


def csv_download(request):
    yesterday = (datetime.datetime.today() -
                 datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    two_days = (datetime.datetime.today() -
                datetime.timedelta(days=2)).strftime('%Y-%m-%d')
    three_days = (datetime.datetime.today() -
                  datetime.timedelta(days=3)).strftime('%Y-%m-%d')
    four_days = (datetime.datetime.today() -
                 datetime.timedelta(days=4)).strftime('%Y-%m-%d')
    five_days = (datetime.datetime.today() -
                 datetime.timedelta(days=5)).strftime('%Y-%m-%d')
    six_days = (datetime.datetime.today() -
                datetime.timedelta(days=6)).strftime('%Y-%m-%d')
    seven_days = (datetime.datetime.today() -
                  datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    eight_days = (datetime.datetime.today() -
                  datetime.timedelta(days=8)).strftime('%Y-%m-%d')
    nine_days = (datetime.datetime.today() -
                 datetime.timedelta(days=9)).strftime('%Y-%m-%d')
    ten_days = (datetime.datetime.today() -
                datetime.timedelta(days=10)).strftime('%Y-%m-%d')

    response = HttpResponse(content_type='text/csv')
    response["Content-Disposition"] = 'attachment; filename="OfficeTotals.csv"'

    offices = Office.objects.all().order_by('name')
    info_lst = []
    for office in offices:
        leadsheets = office.leadsheet_set.all()[:20]
        info = {}
        info['name'] = office
        info['yesterday'] = 'N/A'
        info['two_days'] = 'N/A'
        info['three_days'] = 'N/A'
        info['four_days'] = 'N/A'
        info['five_days'] = 'N/A'
        info['six_days'] = 'N/A'
        info['seven_days'] = 'N/A'
        info['eight_days'] = 'N/A'
        info['nine_days'] = 'N/A'
        info['ten_days'] = 'N/A'

        for ls in leadsheets:
            if str(ls.date_added) == yesterday:
                info['yesterday'] = ls.total()
            if str(ls.date_added) == two_days:
                info['two_days'] = ls.total()
            if str(ls.date_added) == three_days:
                info['three_days'] = ls.total()
            if str(ls.date_added) == four_days:
                info['four_days'] = ls.total()

            if str(ls.date_added) == five_days:
                info['five_days'] = ls.total()

            if str(ls.date_added) == six_days:
                info['six_days'] = ls.total()

            if str(ls.date_added) == seven_days:
                info['seven_days'] = ls.total()
            if str(ls.date_added) == eight_days:
                info['eight_days'] = ls.total()
            if str(ls.date_added) == nine_days:
                info['nine_days'] = ls.total()

            if str(ls.date_added) == ten_days:
                info['ten_days'] = ls.total()

        info_lst.append(info)

    writer = csv.writer(response)
    writer.writerow(['Office', yesterday, two_days,
                     three_days, four_days, five_days, six_days, seven_days, eight_days, nine_days, ten_days])

    for item in info_lst:
        writer.writerow([item['name'], item['yesterday'], item['two_days'],
                         item['three_days'], item['four_days'], item['five_days'], item['six_days'], item['seven_days'], item['eight_days'], item['nine_days'], item['ten_days']])

    return response
