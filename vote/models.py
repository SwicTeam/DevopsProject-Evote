from django.db import models
from django.contrib.auth.models import User
# Create your models here.


 

class Position (models.Model):
    position_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.position_name}"

class Candidate(models.Model):
    candidate_number = models.IntegerField(null=True)
    name = models.CharField(max_length=64)
    #votes_counter = models.IntegerField(null=True,editable=False)
    votes_counter = models.IntegerField(default=0)
    position = models.ForeignKey(Position, null=True, on_delete= models.SET_NULL)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.candidate_number}  {self.name} {self.votes_counter} {self.position} {self.image} "


class EligibleId (models.Model):
    cin = models.BigIntegerField(null=True)
    eligible_user = models.OneToOneField(User,null=True, on_delete= models.SET_NULL)
    voter_has_voted = models.BooleanField(default=False)
    date_voting = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"{self.cin} {self.eligible_user} {self.voter_has_voted} {self.date_voting}"

class Vote(models.Model):
    candidate_vote = models.OneToOneField(Candidate,null=True,on_delete= models.SET_NULL)
    eligibleId = models.OneToOneField(EligibleId,null=True,on_delete= models.SET_NULL)
    def __str__(self):
        return f"{self.candidate_vote} {self.eligibleId}"
    