from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AuthorSerializer, BookSeralizer
from .models import Author, Book

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method == 'GET':
        return Response({'message':'public can view this data'})
    elif request.method == 'POST':
        return Response({"message":f'data created by {request.user.username}.'})
