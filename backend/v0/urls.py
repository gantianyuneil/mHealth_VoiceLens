from django.urls import path
from . import views

urlpatterns = [
    path('', views.toIndex_view),
    path('login/', views.toLogin_view),
    path('register/', views.toRegister_view),
    path('upload/', views.toUpload_view)
]
