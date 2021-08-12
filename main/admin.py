from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from main.models import User, Team, Player, Coach, Match

admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Coach)
admin.site.register(Match)