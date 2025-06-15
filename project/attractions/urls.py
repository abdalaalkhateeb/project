from django.urls import path
from .views import AttractionList, AttractionDetail

urlpatterns = [
    path('', AttractionList.as_view()),
    path('<int:pk>/', AttractionDetail.as_view()),
]