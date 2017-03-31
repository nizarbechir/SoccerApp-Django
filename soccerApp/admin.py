from django.contrib import admin
from .models import Team
from .models import Player
from .models import Match


class MatchAdmin(admin.ModelAdmin):
	list_display = ["__str__","date"]
	list_filter = ["date"]
	class Meta(object):
		model = Match
			


admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match,MatchAdmin)

admin.site.site_header = 'Soccer Ytec administration'