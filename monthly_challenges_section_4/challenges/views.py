from django.shortcuts import render
import logging
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Hello this is january",
    "february": "Hello this is february",
    "march": "Hello this is march",
    "april": "Hello this is april",
    "may": "Hello this is may",
    "june": "Hello this is june",
    "july": "Hello this is july",
    "august": "Hello this is august",
    "september": "Hello this is september",
    "october": "Hello this is october",
    "november": "Hello this is november",
    "december": "Hello this is december"
}

# Create your views here.

# def january(request):
#     return HttpResponse("Hello world")
#

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # If you want to return HTML
    # response_data = """
    #     <ul>
    #         <li><a href="/challenges/"></a></li>
    #     <ul>
    # """

    response_data = f"<ul>{list_items}</url>"

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    # Get index / keys of list
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    # minus one for index referencing
    redirect_month = months[month - 1]
    # reverse first param takes the name value used in url.py
    # reverse second param takes arguments
    # reverse creates path /challenge/1
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenges_text = HttpResponse(monthly_challenges[month])
        response_data = render_to_string("challenges/challenge.html")
    except Exception as ex:
        logging.error('Failed.', exc_info=ex)
        return HttpResponseNotFound(f"Could not find {month}")
    return HttpResponse(response_data)

