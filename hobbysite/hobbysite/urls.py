from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wiki/', include('wiki.urls', namespace="wiki")),
    path('blog/', include('blog.urls', namespace="blog")),
    path('commissions/', include('commissions.urls', namespace="commissions")),
    path('forum/', include('forum.urls', namespace="forum")),
    path('', include('merchstore.urls', namespace="merchstore")),
    path('accounts/', include ('django.contrib.auth.urls')),
    path('user_management/', include('user_management.urls', namespace="user_management")),
    path('homepage/', include('homepage.urls', namespace="homepage")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)