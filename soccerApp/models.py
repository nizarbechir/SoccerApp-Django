from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse



class Team(models.Model):
	"""docstring for Team"""
	nameTeam = models.CharField(max_length=200)
	summary = models.CharField(max_length=400)
	playedGames = models.IntegerField(default=0)
	totalPoint = models.IntegerField(default=0)
	totalVictories = models.IntegerField(default=0)


	def __str__(self):
		return self.nameTeam

	def setTotalPoint(self,name, val):
		team=Team.objects.get(nameTeam = name)
		team.totalPoint +=val
		if(val!=1):
			team.totalVictories +=1
		team.save()

	def setPlayedGames(self,name):
		team=Team.objects.get(nameTeam = name)
		team.playedGames +=1
		team.save()

	def pair(x):
		return not bool(x % 2)

	def save(self, *args, **kwargs):
		ch=""

		myList=Team.objects.order_by('-totalPoint')
		for i,elt in enumerate(myList) :
			print (str(i)+""+elt.nameTeam)
			if not bool(i % 2):
				ch += " | "+elt.nameTeam
			else:
				ch += " VS "+elt.nameTeam

		print (ch)
		listOfMatch = Match.objects.all()
		for match in listOfMatch:
			match.setList(ch)

		super(Team, self).save(*args, **kwargs)



		

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
	list1 = models.CharField(max_length=200,default="ho")
	list2 = models.CharField(max_length=200,default="ho")

	def save(self, *args, **kwargs):
		if (self.nbGoals1 > self.nbGoals2):
			self.team1.setTotalPoint(self.team1.nameTeam,2)
		if (self.nbGoals1 < self.nbGoals2):
			self.team2.setTotalPoint(self.team2.nameTeam,2)
		if (self.nbGoals1 == self.nbGoals2):
			self.team1.setTotalPoint(self.team1.nameTeam,1)
			self.team2.setTotalPoint(self.team2.nameTeam,1)
		self.team1.setPlayedGames(self.team1.nameTeam)
		self.team2.setPlayedGames(self.team2.nameTeam)
		super(Match, self).save(*args, **kwargs)

	def setList(self,listp, *args, **kwargs):
		self.list1=listp
		super(Match, self).save(*args, **kwargs)



	def clean(self):
		if self.team1 == self.team2:
			raise ValidationError('the two teams cannot be the same')


	def __str__(self):
		return self.team1.nameTeam+" VS "+self.team2.nameTeam
		
