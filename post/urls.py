from django.urls import path
from  .views import CategoryView, CategoryListView, LikeView
from .views import HomeView, PostView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView


urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostView.as_view(), name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('post/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/remove/', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
]
