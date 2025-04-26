from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='home'),  # This will map the root URL to the post_list view
    path('posts/<int:pk>/', views.post_detail, name='post-detail-web'),  # URL for viewing a single post
    path('api/posts/', views.PostListCreateView.as_view(), name='post-list-create'),  # API endpoint for listing and creating the posts
    path('api/posts/<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),  # API endpoint for retrieving, updating, and deleting posts
    path('swagger/', views.schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI for API docs
    path('redoc/', views.schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc UI for API docs
]


