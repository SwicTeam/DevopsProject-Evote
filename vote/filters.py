import django_filters
from .models import *

class CandidateFilter(django_filters.FilterSet):
    class Meta:
        model = Candidate
        fields = ['candidate_number', 'name','position']

class CinFilter(django_filters.FilterSet):
    class Meta:
        model = EligibleId
        fields = ['cin']