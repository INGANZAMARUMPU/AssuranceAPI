from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import (
								api_view, 
								authentication_classes,
								permission_classes
								)
from .serializers import *
from .models import *

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class ClientViewSet(viewsets.ModelViewSet):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

class AssuranceViewSet(viewsets.ModelViewSet):
	queryset = Assurance.objects.all()
	serializer_class = AssuranceSerializer

	def update(self, request, pk=None):
		no_police = request.POST["no_police"]
		montant = request.POST["montant"]
		debut = request.POST["debut"]
		plaque = request.POST["plaque"]
		CNI = request.POST["CNI"]
		fin = request.POST["fin"]

		client = Client.objects.get(CNI=CNI)
		materiel = MaterielRoulant.objects.get(plaque=plaque)

		assurance = Assurance.objects.get(id=pk)

		assurance.no_police=no_police
		assurance.montant=montant
		assurance.debut=debut
		assurance.materiel=materiel
		assurance.client=client
		assurance.fin=fin

		assurance.save()
		return Response([{"success": 'updated succesfully'}])

	def create(self, request, *args, **kwargs):
		no_police = request.POST["no_police"]
		montant = request.POST["montant"]
		debut = request.POST["debut"]
		plaque = request.POST["plaque"]
		CNI = request.POST["CNI"]
		fin = request.POST["fin"]

		client = Client.objects.get(CNI=CNI)
		materiel = MaterielRoulant.objects.get(plaque=plaque)
		Assurance(no_police=no_police, montant=montant, debut=debut,
					materiel=materiel, client=client, fin=fin).save()

		return Response([{"success": 'created succesfully'}])

class MaterielViewSet(viewsets.ModelViewSet):
	queryset = MaterielRoulant.objects.all()
	serializer_class = MaterielRoulantSerializer

	def update(self, request, pk=None):
		nom = request.POST['nom']
		plaque = request.POST['plaque']
		chassis = request.POST['chassis']
		roues = request.POST['roues']
		CNI = request.POST['CNI']

		client = Client.objects.get(CNI=CNI)
		materiel = MaterielRoulant.objects.get(id=pk)

		materiel.nom = nom
		materiel.plaque = plaque
		materiel.chassis = chassis
		materiel.roues = roues
		materiel.CNI = CNI

		materiel.save()
		return Response([{"success": 'updated succesfully'}])

	def create(self, request, *args, **kwargs):
		nom = request.POST['nom']
		plaque = request.POST['plaque']
		chassis = request.POST['chassis']
		roues = request.POST['roues']
		CNI = request.POST['CNI']

		client = Client.objects.get(CNI=CNI)
		MaterielRoulant(nom=nom, plaque=plaque, chassis=chassis,
						roues=roues, client=client).save()

		return Response([{"success": 'created succesfully'}])	

@api_view(["GET",])
def logout(request):
	request.user.auth_token.delete()
	return Response([{"success" : "loged out succesfully"}])

@api_view(["GET",])
def get_client(request, CNI):
	data = {}
	try:
		client = Client.objects.get(CNI=CNI)
		data["result"] = client.nom+' '+client.prenom
	except Exception:
		data['result'] = 'client non trouvé'
	return Response([data])


@api_view(["GET",])
def get_auto(request, plaque):
	data = {}
	try:
		auto = MaterielRoulant.objects.get(plaque=plaque)
		data["result"] = auto.nom
	except Exception:
		data['result'] = 'automobile non trouvé'
	return Response([data])

@api_view(["POST", "GET"])
@authentication_classes([])
@permission_classes([])
def login(request):
	if request.method=="GET":
		username = request.GET["username"]
		password = request.GET["password"]
	else:
		username = request.POST["username"]
		password = request.POST["password"]

	data = {}
	try:
		user = User.objects.get(username=username)
		if user.check_password(password):
			data["avatar"] = user.agent.avatar.url
			data["organisation"] = user.agent.organisation.sigle
			try:
				token = Token.objects.create(user=user)
				token.save()
			except:
				token=Token.objects.get(user=user)
			data['username'] = user.username
			data['email'] = user.email
			data['firstname'] = user.first_name
			data['lastname'] = user.last_name
			data["Token"] = token.key
	except Exception as e:
		data["erreur"] = str(e)
	return Response([data])