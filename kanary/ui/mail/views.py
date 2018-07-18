from django.shortcuts import render_to_response
from django.contrib import admin
from django.conf.urls import patterns
from datetime import datetime, date


def creative_sent_for_audit(request):
    return render_to_response(
        'emails/creative_sent_for_audit.html',
        {
            'strategies': ['Coca Cola', 'Hop Cola'],
            'estimated_audit_time': datetime(year=2014, month=3, day=11)
        }
    )


def creative_audit_rejected(request):
    return render_to_response(
        'emails/creative_rejected.html',
        {
            'strategies': ['Coca Cola', 'Hop Cola'],
            'creative': {'appnexus_feedback': 'Offensive content'}
        }
    )


def new_invoice(request):
    return render_to_response(
        'emails/new_invoice.html',
        {'invoice': {'number': 7, 'datetime': datetime.utcnow()}}
    )


def no_sufficient_funds(request):
    return render_to_response('emails/no_sufficient_funds.html')


def no_sufficient_funds_reminder(request):
    return render_to_response('emails/no_sufficient_funds_reminder.html')


def payment_successful(request):
    return render_to_response(
        'emails/payment_successful.html',
        {'payment_amount': 1000.0, 'account_balance': 1500.0}
    )


def reset_password(request):
    return render_to_response(
        'emails/reset_password.html',
        {'reset_link': 'http://gravity/reset_password'}
    )


def welcome(request):
    return render_to_response('emails/welcome.html')


def lotame_report_with_csv(request):
    return render_to_response('emails/lotame_report.html',
                              {'period': date(2014, 1, 15), 'has_csv': True})


def lotame_report_without_csv(request):
    return render_to_response('emails/lotame_report.html',
                              {'period': date(2014, 1, 15), 'has_csv': False})


def get_admin_urls(urls):
    def get_urls():
        my_urls = patterns(
            '',
            (r'^creative_sent_for_audit/$', admin.site.admin_view(creative_sent_for_audit)),
            (r'^creative_audit_rejected/$', admin.site.admin_view(creative_audit_rejected)),
            (r'^lotame_report_with_csv/$', admin.site.admin_view(lotame_report_with_csv)),
            (r'^lotame_report_without_csv/$', admin.site.admin_view(lotame_report_without_csv)),
            (r'^new_invoice/$', admin.site.admin_view(new_invoice)),
            (r'^no_sufficient_funds/$', admin.site.admin_view(no_sufficient_funds)),
            (r'^no_sufficient_funds_reminder/$', admin.site.admin_view(no_sufficient_funds_reminder)),
            (r'^payment_successful/$', admin.site.admin_view(payment_successful)),
            (r'^reset_password/$', admin.site.admin_view(reset_password)),
            (r'^welcome/$', admin.site.admin_view(welcome)),

        )

        return my_urls + urls
    return get_urls
