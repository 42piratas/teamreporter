from django.contrib.auth.models import User
from django.db import models

class UserMethods(User):
    def format_for_js(self):
        return {"email": self.email, "name": self.name, "id": self.id}
    class Meta:
        proxy = True

class Team(models.Model):
    name = models.CharField(max_length=30)
    admin = models.ForeignKey(User, related_name='+')
    users = models.ManyToManyField(User)

    class Meta:
        unique_together = (("admin", "name"))

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.admin)


class Report(models.Model):
    team = models.ForeignKey(Team)

class Question(models.Model):
    report = models.ForeignKey(Report)
    text = models.TextField()
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Survey(models.Model):
    slug = models.SlugField()
    report = models.ForeignKey(Report)
    user = models.ForeignKey(User)
    completed = models.DateTimeField(null=True, blank=True)
    date = models.DateField()


class Answer(models.Model):
    question = models.ForeignKey(Question)
    survey = models.ForeignKey(Survey)
    text = models.TextField()
