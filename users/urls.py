from django.urls import path
from users import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test_view, name='test'),
    path('create/', views.create_product, name="create-product-view"),
    path("update/<int:id>/", views.update_product, name="update_product"),
    path("delete/<int:id>/", views.delete_product, name="delete_product"),
]

