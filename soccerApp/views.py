from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Team,Player,Match
from datetime import timedelta
from django.utils import timezone
from django.db.models import Max,Min,Sum

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# def index(request):
# 	all_team=Team.objects.all()
# 	return render(request,'soccerApp/index.html', {'all_team':all_team})

# def statics(request):
# 	return render(request,'soccerApp/statics.html')



# def team(request, team_id):
# 	team = get_object_or_404(Team,pk=team_id)
# 	return render(request,'soccerApp/details.html', {'team':team})


class IndexView(generic.ListView):
	"""docstring for IndexView"""
	template_name = 'soccerApp/index.html'
	context_object_name = "all_teams"
	maxPoints = Team.objects.order_by('-totalPoint')[0].totalPoint


	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['maxPoints'] = self.maxPoints
		return context
	

	def get_queryset(self):
		return Team.objects.order_by('-totalPoint','playedGames')

class DetailsView(generic.DetailView):
	"""docstring for DetailsView"""
	model = Team
	template_name = 'soccerApp/details.html'


class StaticsView(generic.ListView):
	"""docstring for IndexView"""
	template_name = 'soccerApp/statics.html'
	context_object_name = "all_matchs"
	some_day_last_week = timezone.now().date() - timedelta(days=7)
	monday_of_last_week = some_day_last_week - timedelta(days=(some_day_last_week.isocalendar()[2] - 1))
	monday_of_this_week = monday_of_last_week + timedelta(days=7)
	# if (Match.objects.filter(date__gte=monday_of_last_week, date__lt=monday_of_this_week)):
	minGoal1 = Match.objects.filter(date__gte=monday_of_last_week, date__lt=monday_of_this_week).order_by('nbGoals1')[0].nbGoals1
	minGoal2 = Match.objects.filter(date__gte=monday_of_last_week, date__lt=monday_of_this_week).order_by('nbGoals2')[0].nbGoals2
	maxGoal1 = Match.objects.filter(date__gte=monday_of_last_week, date__lt=monday_of_this_week).order_by('-nbGoals1')[0].nbGoals1
	maxGoal2 = Match.objects.filter(date__gte=monday_of_last_week, date__lt=monday_of_this_week).order_by('-nbGoals2')[0].nbGoals2
	nbrMatch = Match.objects.filter(date__gte=monday_of_last_week, date__lt=monday_of_this_week).count()
	sumGoal  = Match.objects.filter(date__gte=monday_of_last_week, date__lt=monday_of_this_week).aggregate(Sum('nbGoals1'))
	bestTeam = Team.objects.order_by('-totalPoint','playedGames')[0].nameTeam
	badTeam  = Team.objects.order_by('totalPoint')[0].nameTeam
	maxPoints = Team.objects.order_by('-totalPoint')[0].totalPoint
	minPoints = Team.objects.order_by('totalPoint')[0].totalPoint


	def get_queryset(self):	
		return Match.objects.filter(date__gte=self.monday_of_last_week, date__lt=self.monday_of_this_week)

	def get_context_data(self, **kwargs):
		context = super(StaticsView, self).get_context_data(**kwargs)
		context['minG1'] = self.minGoal1
		context['minG2'] = self.minGoal2
		context['maxG1'] = self.maxGoal1
		context['maxG2'] = self.maxGoal2
		context['nbrMatch'] = self.nbrMatch
		context['sumGoal'] = self.sumGoal
		context['bestTeam'] = self.bestTeam
		context['badTeam'] = self.badTeam
		context['maxPoints'] = self.maxPoints
		context['minPoints'] = self.minPoints
		return context



		