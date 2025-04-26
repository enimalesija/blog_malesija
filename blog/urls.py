from django.contrib import admin
from django.urls import path
from posts import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema view for Swagger / ReDoc
schema_view = get_schema_view(
   openapi.Info(
      title="A.Malesija Blog API",
      default_version='v1',
      description="API documentation for the Blog API",
      contact=openapi.Contact(email="emalesija@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='home'),  # Home page displaying posts
    path('posts/<int:pk>/', views.post_detail, name='post-detail-web'),  # URL for single post
    path('api/posts/', views.PostListCreateView.as_view(), name='post-list-create'),  # API: List and create posts
    path('api/posts/<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),  # API: Retrieve, update, and delete posts
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI for API documentation
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # ReDoc UI for API documentation
]
