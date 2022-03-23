from django.urls import path
from django.urls import path
from . import views
urlpatterns=[
    
    path('',views.password, name='password'),
    path('about/',views.about, name='about'),
]

