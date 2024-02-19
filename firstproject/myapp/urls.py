from django.urls import path
from .views import *
from . import views
urlpatterns=[
    # path("hello/",hello),
    # path("index/",index)
    path("hello/",views.hello),
    path("index/",views.index),
    path("contact/",views.contact),
    path("about/",views.about),
    path("test/",views.test),
    path("add/",views.add),
    path("calc/",views.calc),
    path("form/",views.form),
    path("c/",views.customer_detail),
    path("stat/",views.static),
    path('create/', views.create_blog),
    
]