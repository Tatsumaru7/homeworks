from django_filters import rest_framework as filters
from students.models import Course

class CourseFilter(filters.FilterSet):

    id = filters.NumberFilter(field_name='id')

    class Meta:
        model = Course
        fields = ['id', 'name']
