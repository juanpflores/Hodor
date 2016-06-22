from django.views.generic import ListView

from cultures.models import Culture

from quizzes.models import Question, Answer


class QuizView(ListView):

    model = Question
    context_object_name = 'questions'
    template_name = 'quiz.html'

    def get_queryset(self):
        questions = Question.objects.filter(
            culture=Culture.objects.get(name__icontains=self.kwargs['name'])
        )
        return questions

    def get_context_data(self, **kwargs):
        context = super(QuizView, self).get_context_data(**kwargs)
        questions = self.get_queryset()
        answers = []
        for q in questions:
            a = Answer.objects.filter(question=q.pk)
            answers.append(a)
        context['answers'] = answers
        print(context)
        return context
