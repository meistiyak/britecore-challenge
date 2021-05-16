from rest_framework.generics import RetrieveAPIView, ListCreateAPIView

from .models import Risk
from .serializers import RiskSerializer


class RiskListViewSet(ListCreateAPIView):
    serializer_class = RiskSerializer
    queryset = Risk.objects.all()


class RiskDetailViewSet(RetrieveAPIView):
    serializer_class = RiskSerializer
    queryset = Risk.objects.all()
