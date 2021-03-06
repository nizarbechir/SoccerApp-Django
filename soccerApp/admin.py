from django.contrib import admin
from .models import Team
from .models import Player
from .models import Match


class MatchAdmin(admin.ModelAdmin):
	list_display = ["__str__","date"]
	list_filter = ["date"]
	readonly_fields=('list1','list2',)
	class Meta(object):
		model = Match

		

class TeamAdmin(admin.ModelAdmin):
	readonly_fields=('playedGames','totalPoint','totalVictories',)

			


admin.site.register(Team,TeamAdmin)
admin.site.register(Player)
admin.site.register(Match,MatchAdmin)

admin.site.site_header = 'Soccer Ytec administration'