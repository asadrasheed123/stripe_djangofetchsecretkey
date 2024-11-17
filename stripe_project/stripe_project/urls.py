from django.contrib import admin
from django.urls import path, include
from payments.views import homepage  # Import the homepage view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payments/', include('payments.urls')),  # Include payments app URLs
    path('', homepage, name='homepage'),  # Root URL for the homepage
]
