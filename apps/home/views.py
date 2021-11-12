# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Ad
import datetime


@login_required(login_url="/login/")
def index(request):
    # here we should take all ads related to the user and pass it to html template

    ad1 = Ad(first_name="user1", last_name="kh1", phone_number="09136875776",
                 address="khaghani", start_time=datetime.datetime.now(), end_time=datetime.datetime.now(), 
                 service_type='1', sex="woman")

    ad2 = Ad(first_name="user2", last_name="kh2", phone_number="09136775776",
                 address="khaghani", start_time=datetime.datetime.now(), end_time=datetime.datetime.now(), 
                 service_type='3', sex="man")

    ad3 = Ad(first_name="user3", last_name="kh3", phone_number="09136675776",
                 address="khaghani", start_time=datetime.datetime.now(), end_time=datetime.datetime.now(), 
                 service_type='2', sex="woman")

    ads = [ad1, ad2, ad3]
    context = {'ads': ads}

    html_template = loader.get_template('home/ads.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
