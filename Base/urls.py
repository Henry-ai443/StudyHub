from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('profile/<str:pk>/', views.userProfile, name="user_profile"),

    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create_room/', views.create_room, name="create_room"),
    path('update_room/<str:pk>/', views.update_room, name="update_room"),
    path('delete_room/<str:pk>/', views.delete_room, name="delete_room"),
    path('delete_message/<str:pk>/', views.delete_message, name="delete_message"),

     path('update-user/', views.updateUser, name="update-user"),

      path('topics/', views.topicsPage, name="topics"),

      path('activity/', views.activityPage, name="activity"),
]