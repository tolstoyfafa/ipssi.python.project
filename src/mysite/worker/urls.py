from . import views
from django.urls import path, re_path

app_name = 'worker'
urlpatterns = [
    path('hello', views.home, name='test'),
    re_path(r'ads', views.getAllAds, name='ads'),
    re_path(r'demands', views.demand, name='demands'),
    re_path(r'supplies', views.supply, name='supplies'),
    path('details/<int:ad_id>/', views.details, name='details'),
]
