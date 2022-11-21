from django.contrib import admin
from django.urls import path, include

from scraping.views import home, list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list', list_view, name='list'),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('', home, name='home'),

]
