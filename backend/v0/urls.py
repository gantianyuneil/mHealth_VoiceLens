from django.urls import path
from . import views

urlpatterns = [
    path('', views.toIndex_view),
    path('index/', views.login_view),
    path('login/', views.toLogin_view),
    path('register/', views.register_view),
    path('upload/', views.toUpload_view),
    path('profile/', views.toProfile_view),
    path('logout/', views.logout_view)
]
