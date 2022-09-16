from django.urls import path
from restapi.api import views as api_views
urlpatterns = [
    path('datalar/',api_views.data_list_create_api_view, name='data-list'),
    path('datalar/<int:pk>',api_views.data_detail_api_view, name='data-detail'),
    
]