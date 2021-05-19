from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""

    def get(self,request, format=None):
        """ Return a list of APIView features"""
        an_apiview = [
        'uses HTTp methods as function (get, post, patch, put, delete)',
        'IS similar to a traditional Django view',
        'Gives you the most control ovr your application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})




# Create your views here.
