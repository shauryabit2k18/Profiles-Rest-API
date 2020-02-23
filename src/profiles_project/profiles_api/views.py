from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self , request , format = None):
        """returns a list of APIView features"""

        an_apiview = [
            'uses HTTP methods as a function (get , patch , post , put , delete)',
            'it is similar to a traditional Django view',
            'gives you the most control over your logic',
            'its mapped manually to URLs'
        ]

        return Response({'message' : 'hello!!' , 'an_apiview' : an_apiview})
