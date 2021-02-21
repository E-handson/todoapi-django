
from . import views
from rest_framework import routers
from nuxt_api.viewset import TaskViewSet


app_name = 'nuxt_api'
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
