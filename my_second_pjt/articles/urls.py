from django.urls import path
from articles import views

app_name = "articles"
urlpatterns = [
    path('', views.articles, name="articles"),
    path('<int:pk>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('<int:pk>/update/', views.update, name="update"),
	path('<int:pk>/delete/', views.delete, name="delete"),
    path('data-throw/', views.data_throw, name="data-throw"),
    path('data-catch/', views.data_catch, name="data-catch"),
]
