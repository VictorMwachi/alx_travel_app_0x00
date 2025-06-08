from rest_framework import routes
from .views import ListingViewSet, UserViewSet, BookingViewSet
route = routes.DefaultRouter()

route.register('listing',ListingViewSet)
route.register('booking',BookingViewSet)
route.register('user',UserViewSet)

urlpattern = [
    path('',route.urls)
]