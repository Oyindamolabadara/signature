from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
