from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..model.taxis import Taxi  
from ..serializers import TaxiSerializer
from rest_framework.pagination import PageNumberPagination



class TaxisView(APIView):
    pagination_class = PageNumberPagination
    
    def get(self, request):
        plate_filter = request.query_params.get('plate', None)  # Get optional license plate filter
        taxis = Taxi.objects.filter(plate__contains=plate_filter) if plate_filter else Taxi.objects.all()
        serializer = TaxiSerializer(taxis, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)