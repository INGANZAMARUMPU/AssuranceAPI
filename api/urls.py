from django.urls import path, include
from rest_framework import routers
# from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = routers.DefaultRouter()
router.register('agents', views.AgentViewSet)
router.register('clients', views.ClientViewSet)
router.register('assurances', views.AssuranceViewSet)
router.register('materiels', views.MaterielViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('login', views.login, name='login'),
	path('logout', views.logout, name='logout')
]
