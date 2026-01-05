# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Student
# from .serializers import StudentSerializers


# from rest_framework import generics, mixins
# from .models import Student
# from .serializers import StudentSerializers


from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


# class StudentListCreateAPI(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers


#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self , request,  *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class StudentRetrievUpdateDeleteAPI(
#     generics.GenericAPIView,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin
# ):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



# class StudentAPI(APIView):

#     def get(self, request, pk=None):
#         # Get single student
#         if pk is not None:
#             try:
#                 student = Student.objects.get(pk=pk)
#                 serializer = StudentSerializers(student)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except Student.DoesNotExist:
#                 return Response(
#                     {"error": "Student not found"},
#                     status=status.HTTP_404_NOT_FOUND
#                 )

#         # Get all students
#         students = Student.objects.all()
#         serializer = StudentSerializers(students, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)



# def student_list(request):
#     students = Student.objects.all()   # ✅ correct
#     serializer = StudentSerializers(students, many=True)
#     return Response(serializer.data)

