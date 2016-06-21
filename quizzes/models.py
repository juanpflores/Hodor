from django.db import models

from cultures.models import Culture


class Question(models.Model):

    culture = models.ForeignKey(Culture)
    question = models.CharField(max_length=500)

    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Question: {question}".format(question=self.question)


class Answer(models.Model):

    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=250)

    is_correct = models.BooleanField(default=False)

    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{answer} from {question}".format(
            answer=self.answer,
            question=self.question
        )
