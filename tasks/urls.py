from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('update_task/<str:pk>/',views.updatetask,name='update_task'),
    path('delete/<str:pk>/',views.deletetask,name='delete'),

    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),


]