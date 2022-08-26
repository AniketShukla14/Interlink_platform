
from django.urls import path
from .views import HomeView, ArticleDetailView,AddPostView,UpdatePostView,DeletePostView

urlpatterns = [
     # path('',views.home,name="home"),
     path('',HomeView.as_view(), name="home"),
     path('redirect/',HomeView.as_view(), name="redirect"),
     path("article/<int:pk>/",ArticleDetailView.as_view(),name='article-detail'),
     path('add_post/',AddPostView.as_view(),name='add_post'),
     path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
     path('article/remove/<int:pk>',DeletePostView.as_view(),name='delete_post'),
]
