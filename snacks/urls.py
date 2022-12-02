from django.urls import path
from .views import SnackListView,SnackDetail
urlpatterns = [
    path('',SnackListView.as_view(),name='snacks'),
    path('<pk>',SnackDetail.as_view(),name='detail')
]