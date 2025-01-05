from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView
from django.utils.html import strip_tags
from django.utils.text import Truncator
from it_solution.form import LatestNewsForm
from it_solution.models import BusinessGrowth, Category, Comment, CostumerFeedbacks, MeetExports, LatestNews, Message, Services, Technology , Project
from django.db.models import Count
from django.utils.safestring import mark_safe
from django import template
from django.contrib import messages

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

    return render(request, "about.html", context)



def servicesview(request):
    business_services= Services.objects.all()

    context = {
        
        "business_services": business_services
    }
    return render(request, "services.html",context)


def projectview(request):
        explore_project= Project.objects.all()


        context = {
            
            "explore_project": explore_project,
            
        }

        return render(request, "project.html", context )


def newsview(request):
    latest_news = LatestNews.objects.annotate(comments=Count("news_comments"))
    for news in latest_news:
        plain_text = strip_tags(news.content)  # Remove HTML tags
        news.preview = Truncator(plain_text).chars(200, truncate='...')  # Show 200 characters
        news.content_length = len(plain_text)

        context = {
              "latest_news": latest_news,
              
        }
    return render(request, "news.html", context )


def contactview(request):
        
        message= Message.objects.all()
        
        context = {
            
            "message": message
            
        }
        return render(request, "contact.html", context )


def commentview(request):
     comments= Comment.objects.all()
     context={
          
          "comment":  comments,
     }
     return render(request,"news-details.html",context )

def cloudcomputing(request):
        return render(request, "cloud-computing.html")

def itconsultancy(request):
        return render(request, "it-consultancy.html")

def customsoftware(request):
    
        return render(request, "custom-software.html")


def newsdetailsview(request, pk):
      data = get_object_or_404(LatestNews, pk=pk)
      comments = Comment.objects.all()
      context = {
            'data': data,
            'comment': comments
      }

     
      
      return render(request, "news-details.html", context)


def projectdetailsview(request):
      flow = get_object_or_404(Project, pk=pk)
      
      context = {
            'flow': flow,
            # 'comment': comments
      }
      return render(request, "project-details.html")




# for d

def adminview(request):
      return render(request,"admin/dashboard.html")


def addnewsview(request):
    if request.method == 'POST':
        # Retrieve data from the form
        title = request.POST.get('title')  # Matches the 'id' in HTML
        description = request.POST.get('content')  # Corrected the field name
        admin = request.POST.get('admin')  # Matches the 'id' in HTML
        image = request.FILES.get('image')  # Matches the file input name
        date = request.POST.get('date')  # Correctly retrieve the date field

        # Debug print for data retrieval
        print(title, description, admin, image, date)

        # Save the news to the database
        if title and description and admin and image and date:
            LatestNews.objects.create(
                title=title,
                content=description,
                admin=admin,
                image=image,
                date=date
            )
            
            return redirect('it_solution:newslist')  # Redirect to a news list page or success page
    
    # For GET requests, show the form
    return render(request, "admin/add_news.html")




def newslistview(request):
    newslist = LatestNews.objects.all()
    context ={
         
           'newslist' : newslist
     }
    return render(request, "admin/news_list.html", context)

def addprojectview(request):
     
    if request.method == 'POST':
        # Retrieve data from the form
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_title = request.POST.get('category')
        image = request.FILES.get('image')

        print(title, description, category_title, image)

        # Find the category object
        category = Category.objects.filter(id=category_title).first()

        # Save the project to the database
        if category and title and description and image:
            Project.objects.create(
                image=image,
                title=title,
                description=description,
                category=category
            )

        return redirect('it_solution:projectlist')  # Redirect to a project list page or success page
    else:
        categories = Category.objects.all()
   
        context ={
            'categories': categories
        }
        return render(request, "admin/add_project.html", context)

def projectlistview(request):
     
    projectlist = Project.objects.all()
    context ={
         
           'projectlist' : projectlist
     }
    return render(request, "admin/project_list.html", context)




def editprojectview(request, project_id):
    project = get_object_or_404(Project, id= project_id)
     
     
    context={
        'project': project,
        'categories':Category.objects.all()
     }
    return render(request, "admin/editproject.html",context)




def delete_project(request, project_id):
    print(project_id, "project id")
    project = get_object_or_404(Project, id=project_id)
    project_name = project.title  # Save name for feedback
    project.delete()  # Delete the project
    messages.success(request, f"Project '{project_name}' has been successfully deleted.")
    return redirect('it_solution:projectlist')  # Replace with your project list view name
    





def editnewsview(request):
     return render(request, "admin/editnews.html")


def delete_news(request, news_id):
    print(news_id, "news id")
    news = get_object_or_404(LatestNews, id=news_id)
    news_title = news.title  # Save name for feedback
    news.delete()  # Delete the project
    messages.success(request, f"News '{news_title}' has been successfully deleted.")
    return redirect('it_solution:newslist')  # Replace with your project list view name