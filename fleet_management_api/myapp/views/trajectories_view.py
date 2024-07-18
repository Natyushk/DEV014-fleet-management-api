from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

class TrajectoriesView(APIView):
    pagination_class = PageNumberPagination
    
    def get(self, request):
        taxi_id = request.query_params.get('taxi_id', None) 
        date = request.query_params.get('date', None) 