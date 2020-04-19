from django.urls import path
from . import views

urlpatterns = [
    path('', views.display, name='display'),
    path('add_todo/', views.add_todo, name='post_add'),
    path('post/', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('contact1/', views.contact1, name='contact1'),
    path('about/', views.about, name='about'),
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
    path('update/<int:pk>', views.Update.as_view(), name='update'),
    path('olderposts/', views.display_older_posts, name='older')
]
