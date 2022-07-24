from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100)

class Stadium(models.Model):
    name = models.CharField(max_length=100)
    sit_number = models.IntegerField(default=100)

class Match(models.Model):
    match_time = models.DateTimeField()
    first_team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='firstTeam')
    second_team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='secondTeam')
    stadium = models.ForeignKey(Stadium,on_delete=models.CASCADE)



class Sit(models.Model):
    number = models.IntegerField(default=0)
    sitted_user = models.ForeignKey(User, null= True,on_delete=models.SET_NULL)
    match = models.ForeignKey(Match,on_delete=models.CASCADE)


