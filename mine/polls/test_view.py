from django.test import TestCase
from django.utils import timezone
from .views import index,create_question
import datetime
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_index_view_with_no_questions(client):
    response = client.get(reverse('polls:index'))
    assert response.status_code == 200
    assert response== "No polls are available."
    assert response.context['latest_question_list'] == []

@pytest.mark.django_db
def test_index_view_with_a_past_question(client):
    create_question(question_text="Past question.", days=-30)
    response = client.get(reverse('polls:index'))
    assert response.context['latest_question_list']== ['<Question:"Past question">']


@pytest.mark.django_db
def test_index_view_with_a_future_question(client):
    response = client.get(reverse('polls:index'))
    assert response== "No polls are available."
    assert response.context['latest_question_list']== []

@pytest.mark.django_db
def test_index_view_with_future_question_and_past_question(client):
    create_question(question_text="Past question.", days=-30)
    create_question(question_text="Future question.", days=30)
    response = client.get(reverse('polls:index'))
    assert response.context['latest_question_list']== ['<Question: Past question.>']

@pytest.mark.django_db
def test_index_view_with_two_past_questions(client):
    create_question(question_text="Past question 1.", days=-30)
    create_question(question_text="Past question 2.", days=-5)
    response = client.get(reverse('polls:index'))
    assert response.context['latest_question_list']== ['<Question: Past question 2.>', '<Question: Past question 1.>']




    
