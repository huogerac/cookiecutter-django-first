from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [

    url(settings.ADMIN_URL, admin.site.urls),

    url(r'^{{ cookiecutter.first_app_name }}/', include('{{ cookiecutter.first_app_name }}.urls')),

    url(r'^$', RedirectView.as_view(url='/{{ cookiecutter.first_app_name }}/index'), name='{{ cookiecutter.first_app_name }}.index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
