from django.contrib import admin
from django.urls import path, include
from blogs import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.root, name="root"),
    path("blogs/", include("blogs.urls")),
]