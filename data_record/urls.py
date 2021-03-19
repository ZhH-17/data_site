from django.urls import path

from . import views
from .views import IndexView

app_name = 'data_record'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('record/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('record/<int:record_id>/result', views.record_result, name='result'),
]
