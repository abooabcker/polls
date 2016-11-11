
from django.test import TestCase
from django.utils import timezone
from .models import Question
import datetime
import pytest
@pytest.mark.django_db
def test_was_published_recently_with_future_question():
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = Question(pu_date=time)
    future_question.save()
    assert future_question.was_pulished_rescently()== False

@pytest.mark.django_db
def test_was_published_recently_with_old_question():
    time = timezone.now() - datetime.timedelta(days=30)
    old_question = Question(pu_date=time)
    old_question.save()
    assert old_question.was_pulished_rescently()==False

@pytest.mark.django_db
def test_was_published_recently_with_recent_question():
    time = timezone.now() - datetime.timedelta(hours=1)
    recent_question = Question(pu_date=time)
    recent_question.save()
    assert recent_question.was_pulished_rescently()== True

