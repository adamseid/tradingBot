from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fib/', include('fib.urls')),
    path('display/', include('display.urls')),
    path('mainapp/', include('mainapp.urls')),
    path('tracker/', include('tracker.urls'))
]