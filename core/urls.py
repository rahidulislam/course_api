from django.urls import path
from core.views import CourseViewSet

app_name = 'core'


course_list = CourseViewSet.as_view({
    'get': 'list'
})
course_create = CourseViewSet.as_view({
    'post': 'create'
})
course_detail = CourseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('all/', course_list, name='course-list'),
    path('create/', course_create, name='course-create'),
    path('detail/<int:pk>/', course_detail, name='course-detail')
]
