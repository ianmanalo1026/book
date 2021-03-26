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
                        )
from rest_framework_simplejwt.views import (
                                            TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView,
                                            )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/book/', BookListView.as_view()),
    path('api/book/create/', BookCreateView.as_view()),
    path('api/book/<int:pk>/detail/', BookDetailView.as_view()),
    path('api/book/<int:pk>/upvote/', UpvoteCreateView.as_view()),
    path('api/book/<int:pk>/update/', BookUpdateView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
