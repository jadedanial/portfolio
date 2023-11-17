from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/<int:category>/<int:pk>/<slug>/',
         views.projectdetail, name='project'),
]
