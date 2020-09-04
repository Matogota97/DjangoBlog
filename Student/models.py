from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.name}"


class Classe(models.Model):
	name = models.CharField(max_length=20)
	school = models.ForeignKey('School', on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} -- {self.school}"

class RegisterStudent(models.Model):
	nom = models.CharField(max_length=50)
	prenom = models.CharField(max_length=20)
	age = models.IntegerField()
	classe = models.ForeignKey('Classe', on_delete=models.CASCADE)
	pictures = models.ImageField(null=True,blank=True,upload_to="images/pictures")

	def __str__(self):
		
		return f"Nom : {self.nom} -- Prenom : {self.prenom} -- {self.age} ans Etudie : {self.classe}"
class Profile(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	age = models.IntegerField()
	matricule = models.CharField(max_length=25)
	pictures = models.ImageField(null=True,blank=True,upload_to="images/pictures")

