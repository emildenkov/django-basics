from django.urls import path, include
from forumApp.posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-post/', views.add_post, name='add-post'),
    path('<int:pk>/', include([
        path('delete-post/', views.delete_post, name='delete-post'),
        path('details-page/', views.details_page, name='details-post'),
        path('edit-post/', views.edit_post, name='edit-post'),
    ]))
]