from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Agent(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(blank=False)
	organisation = models.ForeignKey("Organisation", on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.organisation.sigle} {self.user.first_name} {self.user.last_name}"


class Organisation(models.Model):
    titre = models.CharField(max_length=64)
    sigle = models.CharField(max_length=10)
   
    def __str__(self):
    	return f"{self.sigle} - {self.titre[15]}"

class Client(models.Model):
    nom= models.CharField(max_length=32)
    prenom= models.CharField(max_length=32)
    CNI= models.CharField(max_length=16, unique=True)
    avatar = models.ImageField(upload_to="avatars")
    email = models.EmailField(null=True)
    depuis = models.DateField(default=timezone.now)
    materiel = models.ManyToManyField("MaterielRoulant", through="Assurance", null=True)

    def __str__(self):
    	return f"{self.nom} {self.prenom}"

class Assurance(models.Model):
    no_police= models.CharField(max_length=100)
    montant= models.CharField(max_length=100)
    debut = models.DateField(verbose_name='debut de validité', default=timezone.now)
    materiel = models.ForeignKey("MaterielRoulant", on_delete=models.CASCADE)
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    fin = models.DateField(verbose_name='date d\'expiration', default=timezone.now)

    def __str__(self):
    	return f"{self.materiel} - {self.client}"

class MaterielRoulant(models.Model):
	nom = models.CharField(max_length=100)
	plaque = models.CharField(max_length=100)
	chassis = models.CharField(max_length=100)
	roues = models.IntegerField(verbose_name='nombre de roues')

	def __str__(self):
		return f"{self.materiel} - {self.client}"