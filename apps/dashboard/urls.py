
from django.urls import path
from . import views
app_name = "dashboard"

urlpatterns = [
    path('home/',views.IndexView.as_view(),name='home')
]
