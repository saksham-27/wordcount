
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='home'),
    path('count/',views.count,name='count'),
    path('About/',views.about,name='about'),
]
