from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('', views.register_view, name="register"),
    path('home/', views.home, name="home"),
    path('logout', views.logout_view, name="logout"),
    path('diary/', views.diary, name="diary"),
    path('mydiary/', views.diary2, name="diary2"),
    path('pictures/', views.pics, name="pics"),
    path('delete/<str:id>', views.delete, name="delete")
]
