from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.contrib import messages

# Create your views here.


def home(request):
    recent_query=Blog.objects.filter(status=1).order_by("-datetimes")[:2]
    context={"recent_query":recent_query}
    return render(request,"polls/index.html",context)


def about(request):
    return render(request,"polls/about.html")

def projects(request):
    return render(request,"polls/projects.html")

def projects2(request):
    return render(request,"polls/projects2.html") 

def blog(request):
    queryset=Blog.objects.filter(status=1).order_by("-datetimes")
    recent_query=Blog.objects.filter(status=1).order_by("-datetimes")[:2]
    featutred_query=Blog.objects.filter(status=1).order_by("-datetimes")[:1]
    p=Paginator(queryset,2)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
   
    context = {'page_obj': page_obj,"recent_query":recent_query,"featured_query":featutred_query}
     
    
    return render(request,"polls/blog.html",context)

def contact(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("Name")
        emailAddress = data.get("EmailAddress")
        subject = data.get("Subject")
        message = data.get("message")

        # Create a new contact entry
        data=Contact.objects.create(Name=name, EmailAddress=emailAddress, Subject=subject, message=message)
        
        # if not all([name, emailAddress, subject, message]):
        #     data.delete()
        #     messages.error(request, "All fields are requird")
        if data:
            data.save()
            messages.success(request, "Submitted Successfully")  
        else:
            messages.error(request, "Not Submitted Successfully")     
       

        return render(request, "polls/contact.html")

    return render(request, "polls/contact.html", {"contact": contact})

def proj1(request):
    return render(request,"polls/proj1.html")

def proj2(request):
    return render(request,"polls/proj2.html")

def proj3(request):
    return render(request,"polls/proj3.html")

def proj4(request):
    return render(request,"polls/proj4.html")

def singlepost(request,slug):
    featutred_query=Blog.objects.filter(status=1).order_by("-datetimes")[:1]
    # post = Blog.objects.get(slug=slug,status=1)
    try:
        post = Blog.objects.get(slug=slug, status=1)
    except Blog.DoesNotExist:
        # If no matching post is found, raise a 404 error
        raise Http404("Blog post does not exist")

    recent_query=Blog.objects.filter(status=1).order_by("-datetimes")[:2]
    return render(request,"polls/singlepost.html", {'post': post,'recent_query':recent_query,"featured_query":featutred_query})