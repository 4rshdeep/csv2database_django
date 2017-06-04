
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myapp/', include('fileupload_app.urls')),
    url(r'^$', RedirectView.as_view(url='myapp/list', permanent=True), name='go-to-myapp'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
