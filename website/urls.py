from django.urls import path
from . import views
from users import views as users_views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('pricing/', views.pricing, name="pricing"),
    path('profile/', views.profile, name="profile"),
    path('update/', users_views.update, name="update"),
    path('procedures/', views.choose_procedure, name="procedures"),
    path('create_appointment/', views.add_visit, name="add_visit"),
]