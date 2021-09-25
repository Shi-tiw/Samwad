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
    upvotes = models.ManyToManyField(User, related_name='upvote', blank=True, null= True )
    views = models.ManyToManyField(User, related_name='view', blank=True, null= True)


    def total_upvotes(self):
        return self.upvotes.count()

    def __str__(self):
        return self.ques

    def get_absolute_url(self):
        return reverse('home')


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='ans_auth')
    answer = models.ForeignKey(Question,related_name="answers", on_delete=models.CASCADE)
    ans_desc = RichTextField(blank=True, null= True)
    date_uploaded = models.DateField(auto_now_add=True)
    upvotes_ans = models.ManyToManyField(User, related_name='upvote_ans',blank=True, null= True )

    def total_upvotes_ans(self):
        return self.upvotes_ans.count()
    
    def __str__(self):
        return '%s - %s' % (self.answer.ques, self.user)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='com_ath')
    answer = models.ForeignKey(Answer,related_name="comforans", on_delete=models.CASCADE,blank=True, null= True)
    question = models.ForeignKey(Question,related_name="comforques", on_delete=models.CASCADE, blank=True, null= True)
    com_desc = RichTextField(blank=True, null= True)
    date_updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.com_desc, self.user)
