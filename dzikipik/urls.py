"""dzikipik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from dzikipik import settings
from main.views import IndexView, BlogView, GalleryView, PricingView, ContactView, LoginView, RegisterView, SessionView, \
    PostView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    url('blog/', BlogView.as_view(), name="blog"),
    url('galeria/', GalleryView.as_view(), name="gallery"),
    url('cennik/', PricingView.as_view(), name="pricing"),
    url('kontakt/', ContactView.as_view(), name="contact"),
    url('login/', LoginView.as_view(), name="login"),
    url('logout/', LogoutView.as_view(), name="logout"),
    url('register/', RegisterView.as_view(), name="register"),
    url('sesja/', SessionView.as_view(), name="session"),
    url('post/(?P<id>(\d)+)', PostView.as_view(), name="post"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)