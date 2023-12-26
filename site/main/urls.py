from django.urls import path, include
from . import views
from .views import RegisterView, LoginView

app_name = 'main'

urlpatterns = [
    path('', views.IndexList.as_view(), name="index"),
    path('service/', views.ServiceList.as_view(), name="service_list"),
    path('service/<int:id>/', views.service, name='service'),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
