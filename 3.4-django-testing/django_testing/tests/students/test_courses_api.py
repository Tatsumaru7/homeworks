import pytest
from rest_framework import status
from students.models import Course
from django.urls import reverse

@pytest.mark.django_db
def test_retrieve_course(api_client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', kwargs={'pk': course.pk})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == course.pk

@pytest.mark.django_db
def test_list_courses(api_client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse('courses-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(courses)

@pytest.mark.django_db
def test_create_course(api_client):
    data = {'name': 'New Course'}
    url = reverse('courses-list')
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Course.objects.filter(name=data['name']).exists()

@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    course = course_factory()
    data = {'name': 'Updated Course'}
    url = reverse('courses-detail', kwargs={'pk': course.pk})
    response = api_client.patch(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert Course.objects.get(pk=course.pk).name == data['name']

@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', kwargs={'pk': course.pk})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Course.objects.filter(pk=course.pk).exists()

# Тест фильтрации по id
@pytest.mark.django_db
def test_filter_course_by_id(api_client, course_factory):
    course = course_factory()
    url = reverse('courses-list')
    response = api_client.get(url, {'id': course.pk})  # Фильтрация по id
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['id'] == course.pk

# Тест фильтрации по названию курса
@pytest.mark.django_db
def test_filter_course_by_name(api_client, course_factory):
    course = course_factory(name='Math Course')
    url = reverse('courses-list')
    response = api_client.get(url, {'name': 'Math Course'})  # Фильтрация по названию
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Math Course'
