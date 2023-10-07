"""
URL configuration for myproject project.

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

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
# In your urls.py file within the myapp app

import debug_toolbar
from django.urls import path
from . import views
from django.urls import include, path



urlpatterns = [
    # ...
    path('donor-info-list/', views.donor_info_list, name='donor_info_list'),

    # Add URL for adding a new donor
    path('donor-add-form/', views.add_donor, name='add_donor'),

    # Add URL for updating a donor
    path('donors/<int:pk>/update/', views.update_donor, name='update_donor'),
    # ...

    path('donor-finder/', views.donor_finder, name='donor_finder'),

    path("__debug__/", include("debug_toolbar.urls")),

]

