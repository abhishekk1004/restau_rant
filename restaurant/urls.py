from django.urls import path
from rest_framework import routers
from .views import *

router= routers.SimpleRouter()

router.register('categories',CategoryViewSet)
router.register('tables', TableViewSet)
router.register('menus',MenuViewSet)
router.register('orders',OrderViewSet)
router.register('waiters',WaiterViewSet)
router.register('receptions',ReceptionViewSet)
urlpatterns = [
    
] +router.urls
