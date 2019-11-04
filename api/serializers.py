from rest_framework import serializers
from django.utils import timezone
from  .models import *

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
    	model = Agent
    	fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = "__all__"


class AssuranceSerializer(serializers.ModelSerializer):
	materiel = serializers.SerializerMethodField()
	client = serializers.SerializerMethodField()
	plaque = serializers.SerializerMethodField()
	class Meta:
		model = Assurance
		fields = ("id","no_police", "montant", "debut", "materiel", "client", "fin", "plaque")

	def get_client(self, obj):
		return str(obj.client.nom+" "+obj.client.prenom)

	def get_materiel(self, obj):
		return str(obj.materiel.nom)

	def get_plaque(self, obj):
		return str(obj.materiel.plaque)

class MaterielRoulantSerializer(serializers.ModelSerializer):

	client = serializers.SerializerMethodField()
	CNI = serializers.SerializerMethodField()

	class Meta:
		model = MaterielRoulant
		fields =("nom", "plaque", "chassis", "roues", "client", "CNI")

	def get_client(self, obj):
		return str(obj.client)

	def get_CNI(self, obj):
		return str(obj.client.CNI)