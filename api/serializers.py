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
	class Meta:
		model = Assurance
		fields = "__all__"#("id","no_police", "montant", "debut", "materiel", "client", "fin")

	def get_client(self, obj):
		return str(obj.client)

	def get_materiel(self, obj):
		return str(obj.materiel)

class MaterielRoulantSerializer(serializers.ModelSerializer):

	client = serializers.SerializerMethodField()

	class Meta:
		model = MaterielRoulant
		fields ="__all__"

	def get_client(self, obj):
		return str(obj.client)
