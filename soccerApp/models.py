from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse



class Team(models.Model):
	"""docstring for Team"""
	nameTeam = models.CharField(max_length=200)
	summary = models.CharField(max_length=400)
	playedGames = models.IntegerField()
	totalPoint = models.IntegerField()
	totalVictories = models.IntegerField()


	def __str__(self):
		return self.nameTeam

	def __setattr__(self, attrname, val):

		super(Team, self).__setattr__(attrname, val)

	# def set_totalPoint(self):
	# 	self.totalPoint +=2;
		

class Player(models.Model):
	"""docstring for Player"""
	namePlayer = models.CharField(max_length=200)
	nbGoal = models.IntegerField()
	team = models.ForeignKey(Team, on_delete=models.CASCADE)	
	def __str__(self):
		return self.namePlayer
		

class Match(models.Model):
	"""docstring for Match"""
	team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
	team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
	date = models.DateTimeField()
	nbGoals1 = models.IntegerField()
	nbGoals2 = models.IntegerField()

	def save(self, *args, **kwargs):
		if (self.nbGoals1 > self.nbGoals2):
			self.team1.totalPoint +=2
			self.team1.totalVictories +=1
		if (self.nbGoals1 < self.nbGoals2):
			self.team2.totalPoint +=2
			self.team2.totalVictories +=1
		if (self.nbGoals1 == self.nbGoals2):
			self.team1.totalPoint +=1
			self.team2.totalPoint +=1
		self.team1.playedGames +=1
		self.team2.playedGames +=1
		super(Match, self).save(*args, **kwargs)



	def clean(self):
		if self.team1 == self.team2:
			raise ValidationError('the two teams cannot be the same')


	def __str__(self):
		return self.team1.nameTeam+" VS "+self.team2.nameTeam
		
