
from django.test import TestCase
from django.utils import timezone
from .models import Questions
from datetime import datetime,timedelta
from django.urls import reverse
# Create your tests here.


class QuestionsModelTests(TestCase):

    def test_was_pub_recently_with_future_question(self):
        time = timezone.now()+timedelta(days=30)
        future_question = Questions(pud_date = time)

        self.assertIs(future_question.was_published_recently(),False)


def create_question(question_text,days):
    time=timezone.now()+ timedelta(days=days)
    return Questions.objects.create(question_text=question_text,pud_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'],[])
    def test_past_question(self):
        create_question("Past question",-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],['<Questions: Past question>'])
    def test_future_question(self):
        create_question("Future question",30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response,'No polls are available')
    def test_future_and_past_question(self):
        create_question("Past question",-30)
        create_question("Future question",30)
        response=self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],['<Questions: Past question>'])

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Questions: Past question 2.>', '<Questions: Past question 1.>']
        )
    # def test_question_with_no_choice(self):


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question("future question",5)
        url = reverse('polls:detail',args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code,404)

    def test_past_question(self):
        past_question = create_question('Past question',-5)
        url = reverse('polls:detail',args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response,past_question.id)