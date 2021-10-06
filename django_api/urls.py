"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

# from test_app.views import SimpleViewset #SimpleGenerics, #SimpleGenericsUpdate, #,Simple

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register("simple-viewset", SimpleViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('simple/', Simple.as_view()),
    # path('simple/<int:id>', Simple.as_view()),
    # path('simple-generics', SimpleGenerics.as_view()),
    # path('simple-generics/<int:id>', SimpleGenericsUpdate.as_view()), #with <int:id> an error of pk is returned therefore need for lookup_field, but <int:pk> works perfectly without lookup_field
    # path("", include(router.urls)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls))
    ] + urlpatterns