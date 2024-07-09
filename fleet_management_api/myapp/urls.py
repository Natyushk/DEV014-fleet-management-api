from django.urls import path
from .views import TaxisView, TrajectoriesView
from rest_framework import permissions
##from drf_yasg.views import get_schema_view
##from drf_yasg import openapi

urlpatterns = [
    path('taxis/', TaxisView.as_view(), name='taxis-list'),
    path('trajectories/', TrajectoriesView.as_view(), name='taxis-list'),
    ##path('swagger/', get_swagger_view.SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ##path('swagger/', schema_view, name='schema-swagger-ui')
]