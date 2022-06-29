from django.shortcuts import render
import logging
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    "december": None
}

# Create your views here.

# def january(request):
#     return HttpResponse("Hello world")
#


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


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
        challenges_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenges_text,
            "month_name": month
        })
    except Exception as ex:
        logging.error('Failed.', exc_info=ex)
        return HttpResponseNotFound(f"Could not find {month}")

