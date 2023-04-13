from django.urls import path

from django_blog.article import views

urlpatterns = [
    path('', views.IndexPageView.as_view()),
    path('<slug:tag>/<int:article_id>/', views.IndexPageView.as_view(), name='article'),
]
