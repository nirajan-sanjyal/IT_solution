from django.shortcuts import render
from django.views.generic import ListView
from django.utils.html import strip_tags
from django.utils.text import Truncator
from it_solution.models import BusinessGrowth, CostumerFeedbacks, MeetExports, LatestNews, Services, Technology , Project
from django.db.models import Count
from django.utils.safestring import mark_safe
from django import template

register = template.Library()

# Create your views here.




def homeview(request):
    latest_news = LatestNews.objects.annotate(comments=Count("news_comments"))
    for news in latest_news:
        plain_text = strip_tags(news.content)  # Remove HTML tags
        news.preview = Truncator(plain_text).chars(200, truncate='...')  # Show 200 characters
        news.content_length = len(plain_text)
        

        meet_exports= MeetExports.objects.all()

        explore_project= Project.objects.all()

        
        business_services= Services.objects.all()

    context = {
        "latest_news": latest_news,
        "meet_exports": meet_exports,
        "logos": Technology.objects.all(),
        "explore_project": explore_project,
        "business_services": business_services
    }

    return render(request, "home/index.html", context)



def aboutview(request):

    meet_exports= MeetExports.objects.all()
    growth_business= BusinessGrowth.objects.last()
    costumer_feedbacks= CostumerFeedbacks.objects.all()
    context = {
       
        "logos": Technology.objects.all(),
        "meet_exports": meet_exports,
        "growth_business": growth_business,
        "costumer_feedbacks": costumer_feedbacks
        
    }

    return render(request, "about.html", context    )



def servicesview(request):
    return render(request, "services.html")


def projectview(request):
    return render(request, "project.html")


def newsview(request):
    return render(request, "views.html")


def contactview(request):
    return render(request, "contact.html")