"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.urls import include

# from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("captcha/", include("captcha.urls")),
    path("user/", include("apps.user.urls")),
    path("about/", include("apps.base.urls")),
    path("help-points/", include("apps.project_functionality.urls")),
    path("celery-for-parser/", include("apps.celery_for_parser.urls")),
    path("", include("apps.base.urls_root")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
