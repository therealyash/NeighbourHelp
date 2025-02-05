from django.urls import path
from .views import HomePageView, about, signup_view, createtask, userDash, volDash
from . import views

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path('signup/', signup_view, name='signup'),
    path('about/', about, name='about'),
    path('createtask/', views.createtask, name='createtask'),
    path('userDash/', userDash, name='userDash'), 
    path('volDash/', volDash, name='volDash'), 
    path('accept_task/<int:task_id>/', views.accept_task, name='accept_task'),
    path('decline_task/<int:task_id>/', views.decline_task, name='decline_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    

]
