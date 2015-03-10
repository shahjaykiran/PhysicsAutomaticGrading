import datetime

from django.db import models
from django.utils import timezone

class Homework(models.Model):
    HW_ID = models.AutoField(primary_key=True)
    HW_Number = models.IntegerField(default=0)
    HW_Submission_Date = models.DateTimeField('submission date')
    HW_Timestamp = models.DateTimeField('date published')

class Question(models.Model):
    Question_ID = models.AutoField(primary_key=True)
    Question_HW_Number = models.IntegerField(default=0)
    Question_Number = models.IntegerField(default=0)
    Question_Content = models.TextField()
    Question_Notation = models.TextField()
    Question_Image = models.CharField(max_length=300)
    Question_Timestamp = models.DateTimeField('date published')

class Question_Part(models.Model):
    Question_Part_ID = models.AutoField(primary_key=True)
    Question_Part_HW_Number = models.IntegerField(default=0)
    Question_Part_Q_Number = models.IntegerField(default=0)
    Question_Part_Number = models.IntegerField(default=0)
    Question_Part_Content = models.TextField()
    Question_Part_Image = models.CharField(max_length=300)
    Question_Part_Points = models.IntegerField(default=0)
    Question_Part_Timestamp = models.DateTimeField('date published')

class Question_Hint(models.Model):
    Question_Hint_ID = models.AutoField(primary_key=True)
    Question_Hint_HW_Number = models.IntegerField(default=0)
    Question_Hint_Q_Number = models.IntegerField(default=0)
    Question_Hint_QP_Number = models.IntegerField(default=0)
    Question_Hint_Number = models.IntegerField(default=0)
    Question_Hint_Content = models.TextField()
    Question_Hint_Options = models.TextField()
    Question_Hint_Correct_Answer = models.CharField(max_length=100)
    Question_Hint_Timestamp = models.DateTimeField('date published')

class Answers(models.Model):
    Answers_ID = models.AutoField(primary_key=True)
    Answers_Student_ID = models.IntegerField(default=0)
    Answers_HW_Number = models.IntegerField(default=0)
    Answers_Q_Number = models.IntegerField(default=0)
    Answers_QP_Number = models.IntegerField(default=0)
    Answers_Hint_Number = models.IntegerField(default=0)
    Answers_Explaination = models.TextField()
    Answers_Correct_Answer = models.TextField()
    
class Summary(models.Model):
    Summary_ID = models.AutoField(primary_key=True)
    Summary_HW_Number = models.IntegerField(default=0)
    Summary_Content = models.TextField()
    Summary_Timestamp = models.DateTimeField('date published')