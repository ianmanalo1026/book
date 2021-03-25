from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views

from core.views import (
                        BookCreateView,
                        BookListView,
                        UpvoteCreateView,
                        BookDetailView,
                        BookUpdateView,
                        UserRegisterationView,
                        LoginView,
                        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', LoginView.as_view()),
    path('api/register/', UserRegisterationView.as_view()),
    path('api/book/', BookListView.as_view()),
    path('api/book/create/', BookCreateView.as_view()),
    path('api/book/<int:pk>/detail/', BookDetailView.as_view()),
    path('api/book/<int:pk>/upvote/', UpvoteCreateView.as_view()),
    path('api/book/<int:pk>/update/', BookUpdateView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
