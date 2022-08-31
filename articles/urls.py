from .views import HomePageView, BlogDetailView
from django.urls import path

urlpatterns = [
    path("article/<int:pk>/", BlogDetailView.as_view(), name="post_list" ),
    path('', HomePageView.as_view(), name='Home')
]