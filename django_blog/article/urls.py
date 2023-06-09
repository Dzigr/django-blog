from django.urls import path
from django_blog.article import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='articles'),
    path('<int:id>/edit/', views.ArticleFormEditView.as_view(), name='article_edit'),
    path('<int:id>/delete/', views.ArticleFormDeleteView.as_view(), name='article_delete'),
    path('<int:id>/', views.ArticleView.as_view(), name='article_id'),
    path('create/', views.ArticleFormCreateView.as_view(), name='article_create'),
]
