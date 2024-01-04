from django.shortcuts import render
from visitors.models import Visitor
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreateUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
def index(request):

    all_visitors = Visitor.objects.all()

    context = {
        'page_name': 'Dashboard Start',
        'all_visitors': all_visitors,
    }

    return render(request, 'index.html', context=context)