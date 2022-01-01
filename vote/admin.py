from django.contrib import admin

from .models import Candidate, Position, EligibleId, Vote
# Register your models here.
admin.site.register(Candidate)
admin.site.register(Position)
admin.site.register(EligibleId)

