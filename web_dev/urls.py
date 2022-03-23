
from django.contrib import admin
from django.urls import path, include
from passwords import views
urlpatterns = [
    path('',views.home,name='home'),
    path('passwords',include('passwords.urls')),
    path('users/',include('users.urls') ),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
