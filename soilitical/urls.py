from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import  static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    # path('login/', include("accounts.urls")),
    # path('dashboard/', include("dashboard.urls")),
    # path('prediction/', include("prediction.urls")),
]
