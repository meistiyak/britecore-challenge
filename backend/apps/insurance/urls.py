from django.urls import path

from .views import RiskDetailViewSet, RiskListViewSet

urlpatterns = [
    path('risks/', RiskListViewSet.as_view(), name='risk-list-create'),
    path('risks/<int:pk>/', RiskDetailViewSet.as_view(), name='risk-detail')
]
