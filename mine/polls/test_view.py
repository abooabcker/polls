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
    assert "No polls are available." in response.content
    assert list(response.context['latest_question_list']) == []

@pytest.mark.django_db
def test_index_view_with_a_past_question(client):
    ques=create_question(question_text="Past question.", days=-30)
    response = client.get(reverse('polls:index'))
    assert list(response.context['latest_question_list'])==[ques]


@pytest.mark.django_db
def test_index_view_with_a_future_question(client):
    qun=create_question(question_text="future question creation",days=30)
    response = client.get(reverse('polls:index'))
    assert "No polls are available." in response.content
    assert list(response.context['latest_question_list'])== []

@pytest.mark.django_db
def test_index_view_with_future_question_and_past_question(client):
    q1=create_question(question_text="Past question.", days=-30)
    q2=create_question(question_text="Future question.", days=30)
    response = client.get(reverse('polls:index'))
    assert list(response.context['latest_question_list'])== [q1]

@pytest.mark.django_db
def test_index_view_with_two_past_questions(client):
    q1=create_question(question_text="Past question 1.", days=-30)
    q2=create_question(question_text="Past question 2.", days=-5)
    response = client.get(reverse('polls:index'))
    assert list(response.context['latest_question_list'])==[q1,q2] 




    
