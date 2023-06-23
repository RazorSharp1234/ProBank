from django.conf import settings
from django.conf.urls.static import static

from form import views
from django.urls import path

from form.views import form

urlpatterns = [
    # Other URL patterns in your app

    path('form/', form, name='form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)