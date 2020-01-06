
from django.test import TestCase
from django.utils import timezone
from .models import Questions
from datetime import datetime,timedelta
# Create your tests here.


class QuestionsModelTests(TestCase):

    def test_was_pub_recently_with_future_question(self):
        time = timezone.now()+timedelta(days=30)
        future_question = Questions(pud_date = time)
        self.assertIs(future_question.was_published_recently(),False)
