from django.urls import path
from .views import Create, Read, Update, Delete

urlpatterns = [
    path('create', Create.as_view()),
    path('read', Read.as_view()),
    path('update', Update.as_view()),
    path('delete', Delete.as_view())
] 