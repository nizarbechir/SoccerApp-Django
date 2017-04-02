from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Team, Player, Match
from datetime import timedelta
from django.utils import timezone
from django.db.models import Max, Min, Sum

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class IndexView(generic.ListView):
    """docstring for IndexView"""

    template_name = None
    context_object_name = None
    maxPoints = None

    def process(self):
        self.template_name = 'soccerApp/index.html'
        self.context_object_name = "all_teams"
        self.maxPoints = Team.objects.order_by('-totalPoint')[0].totalPoint

    def get_context_data(self, **kwargs):
        self.process()
        context = super(IndexView, self).get_context_data(**kwargs)
        context['maxPoints'] = self.maxPoints
        return context

    def get_queryset(self):
        return Team.objects.order_by('-totalPoint', 'playedGames')


class DetailsView(generic.DetailView):
    """docstring for DetailsView"""
    model = Team
    template_name = 'soccerApp/details.html'


class StaticsView(generic.ListView):
    """docstring for IndexView"""
    template_name = 'soccerApp/statics.html'
    context_object_name = "all_matchs"
    some_day_last_week = None
    monday_of_last_week = None
    monday_of_this_week = None
    # if (Match.objects.filter(date__gte=monday_of_last_week, date__lt=monday_of_this_week)):
    minGoal1 = None
    minGoal2 = None
    maxGoal1 = None
    maxGoal2 = None
    nbrMatch = None
    sumGoal = None
    bestTeam = None
    badTeam = None
    maxPoints = None
    minPoints = None

    def process(self):
        self.template_name = 'soccerApp/statics.html'
        self.context_object_name = "all_matchs"
        self.some_day_last_week = timezone.now().date() - timedelta(days=7)
        self.monday_of_last_week = self.some_day_last_week - timedelta(days=(self.some_day_last_week.isocalendar()[2] - 1))
        self.monday_of_this_week = self.monday_of_last_week + timedelta(days=7)
        # if (Match.objects.filter(date__gte=monday_of_last_week, date__lt=monday_of_this_week)):
        self.minGoal1 = \
        Match.objects.filter(date__gte=self.monday_of_last_week, date__lt=self.monday_of_this_week).order_by('nbGoals1')[
            0].nbGoals1
        self.minGoal2 = \
        Match.objects.filter(date__gte=self.monday_of_last_week, date__lt=self.monday_of_this_week).order_by('nbGoals2')[
            0].nbGoals2
        self.maxGoal1 = \
        Match.objects.filter(date__gte=self.monday_of_last_week, date__lt=self.monday_of_this_week).order_by('-nbGoals1')[
            0].nbGoals1
        self.maxGoal2 = \
        Match.objects.filter(date__gte=self.monday_of_last_week, date__lt=self.monday_of_this_week).order_by('-nbGoals2')[
            0].nbGoals2
        self.nbrMatch = Match.objects.filter(date__gte=self.monday_of_last_week, date__lt=self.monday_of_this_week).count()
        self.sumGoal = Match.objects.filter(date__gte=self.monday_of_last_week, date__lt=self.monday_of_this_week).aggregate(
            Sum('nbGoals1'))
        self.bestTeam = Team.objects.order_by('-totalPoint', 'playedGames')[0].nameTeam
        self.badTeam = Team.objects.order_by('totalPoint')[0].nameTeam
        self.maxPoints = Team.objects.order_by('-totalPoint')[0].totalPoint
        self.minPoints = Team.objects.order_by('totalPoint')[0].totalPoint

    def get_queryset(self):
        self.process()
        return Match.objects.filter(date__gte=self.monday_of_last_week, date__lt=self.monday_of_this_week)

    def get_context_data(self, **kwargs):
        self.process()
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
