from django.shortcuts import get_object_or_404
from core.serializers import CourseSerializer, EnrollmentSerializer
from core.models import Course, Enrollment
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response({'message': 'Course was not created'}, status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        course = get_object_or_404(Course, pk=pk)
        serialzer = self.serializer_class(course, data=request.data, partial=partial)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status.HTTP_200_OK)
        return Response({'message': 'This course is not updated'}, status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def retrieve(self, request, pk, *args, **kwargs):
        course = get_object_or_404(Course, pk=pk)
        serializer = self.serializer_class(course)
        return Response(serializer.data)

    def destroy(self, request, pk, *args, **kwargs):
        course = get_object_or_404(Course, pk=pk)
        if course:
            course.delete()
            return Response({'message': 'Course is Deleted'}, status.HTTP_204_NO_CONTENT)
        return Response({'message': 'Course is not Deleted'}, status.HTTP_400_BAD_REQUEST)
    