from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wiki/', include('wiki.urls', namespace="wiki")),
    path('blog/', include('blog.urls', namespace="blog")),
    path('commissions/', include('commissions.urls', namespace="commissions")),
    path('forum/', include('forum.urls', namespace="forum")),
    path('', include('merchstore.urls', namespace="merchstore")),
    path('accounts/', include ('django.contrib.auth.urls')),
    path('profile/', include('user_management.urls', namespace="user_management")),
]

