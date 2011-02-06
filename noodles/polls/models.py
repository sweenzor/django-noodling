from django.db import models

# Create your models here.
from django.db import models

class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_data = models.DateTimeField('date published')
	def __unicode__(self):
		return self.question

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	def __unicode__(self):
		return self.choice
