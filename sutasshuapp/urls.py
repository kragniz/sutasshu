from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from sutasshuapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
