from django.urls import path
# from . import views
from .views import HomeView, PostView, AddPostView, UpdatePostView


urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('Post/<int:pk>', PostView.as_view(), name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('Post/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
]
