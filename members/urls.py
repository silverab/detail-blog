from django.urls import path
from .views import UserRegisterView, UserEditView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='signup'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]
