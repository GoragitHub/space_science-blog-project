from django.urls import path
from . import views


urlpatterns=[
    path("",views.home, name="home"),
    path("about/",views.about, name="about"),
    path("projects/",views.projects, name="projects"),
    path("projects2/",views.projects2, name="projects2"),
    path("blog/",views.blog, name="blog"),
    path("contact/",views.contact, name="contact"),
    path("proj1/",views.proj1, name="proj1"),
    path("proj2/",views.proj2, name="proj2"),
    path("proj3/",views.proj3, name="proj3"),
    path("proj4/",views.proj4, name="proj4"),
    path("<str:slug>/",views.singlepost, name="singlepost")
   
] 
 