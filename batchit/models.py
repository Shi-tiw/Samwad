from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from datetime import date



class Question(models.Model):
    ques= models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ques_desc = RichTextField(blank=True, null= True)
    datetime = models.DateField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='upvote')
    views = models.ManyToManyField(User, related_name='view')


    def total_upvotes(self):
        return self.upvotes.count()

    def __str__(self):
        return self.ques

    def get_absolute_url(self):
        return reverse('home')


class ComForQues(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='comforques_ath')
    question = models.ForeignKey(Question,related_name="comforques", on_delete=models.CASCADE)
    com_desc = RichTextField(blank=True, null= True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.question.ques, self.user)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='answer')
    answer = models.ForeignKey(Question,related_name="answers", on_delete=models.CASCADE)
    com_desc = RichTextField(blank=True, null= True)
    date_uploaded = models.DateField(auto_now_add=True)
    upvotes_ans = models.ManyToManyField(User, related_name='upvote_ans')

    def total_upvotes_ans(self):
        return self.upvotes_ans.count()
    
    def __str__(self):
        return '%s - %s' % (self.answer.ques, self.user)


class ComForAns(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='comforans_ath')
    answer = models.ForeignKey(Answer,related_name="comforans", on_delete=models.CASCADE)
    com_desc_ans = RichTextField(blank=True, null= True)
    date_updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.answer.com_desc, self.user)
