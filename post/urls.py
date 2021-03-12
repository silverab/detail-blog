from django.urls import path
from  .views import CategoryView, CategoryListView, LikeView
from .views import HomeView, PostView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView


urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('Post/<int:pk>', PostView.as_view(), name='post_detail'),
    path('Add_post/', AddPostView.as_view(), name='add_post'),
    path('Add_category/', AddCategoryView.as_view(), name='add_category'),
    path('Post/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('Post/<int:pk>/remove/', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='category_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
]
