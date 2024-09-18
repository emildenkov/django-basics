from django.urls import path

from urlsAndViews.departments import views

urlpatterns = [
    path('', views.index, name='index'),
    path('redirect-to-index/', views.redirect_to_index, name='redirect_view'),
    path('redirect-to-github', views.redirect_to_github, name='github_redirect'),
    path('<int:pk>/<slug:slug>', views.view_with_int_pk_snd_slug),
    path('<int:pk>', views.view_with_pk),
    path('<slug:slug>', views.view_with_slug),
]