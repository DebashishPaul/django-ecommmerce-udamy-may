
from django.contrib import admin
from django.urls import include, path
from store.views import IndexView, DetailsView, CheckoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name= 'index'),
    path('details:<id>', DetailsView, name='details' ),
    path('checkout/', CheckoutView, name='checkout'),
]
