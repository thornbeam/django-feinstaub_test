"""
URL configuration for feinstaub_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from sensors.models import bme280, bmp180, bmp280

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
class Bme280Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bme280
        fields = "__all__"
class Bmp180Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bmp180
        fields = "__all__"
class Bmp280Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = bmp280
        fields = "__all__"

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class Bme280ViewSet(viewsets.ModelViewSet):
    queryset = bme280.objects.all()
    serializer_class = Bme280Serializer
class Bmp180ViewSet(viewsets.ModelViewSet):
    queryset = bmp180.objects.all()
    serializer_class = Bmp180Serializer
class Bmp280ViewSet(viewsets.ModelViewSet):
    queryset = bmp280.objects.all()
    serializer_class = Bmp280Serializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bme280s', Bme280ViewSet)
router.register(r'bmp180s', Bmp180ViewSet)
router.register(r'bmp280s', Bmp280ViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
