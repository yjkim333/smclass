from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('member/', include('member.urls')),
    path('board/', include('board.urls')),
    path('comment/', include('comment.urls')),
]


# settings.py 안에
# MEDIA_URL = 'media/' 로 들어오면
# MEDIA_ROOT = os.path.join(BASE_DIR,'media') 에서 찾아라
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)