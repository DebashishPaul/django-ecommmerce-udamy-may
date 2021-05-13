
from django.contrib import admin
from django.urls import include, path
from store.views import IndexView, DetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name= 'index'),
    path('details:<id>', DetailsView, name='details' )
]
