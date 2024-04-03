from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentCreateAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RetrieveAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UpdateAPIView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DestroyAPIView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

