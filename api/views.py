from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
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

class MaterielViewSet(viewsets.ModelViewSet):
    queryset = MaterielRoulant.objects.all()
    serializer_class = MaterielRoulantSerializer		

# class UserViewSet(viewsets.ViewSet):
#     def list(self, request):
#         pass
#     def create(self, request):
#         pass
#     def retrieve(self, request, pk=None):
#         pass
#     def update(self, request, pk=None):
#         pass
#     def partial_update(self, request, pk=None):
#         pass
#     def destroy(self, request, pk=None):
#         pass

@api_view(["GET",])
def logout(request):
	request.user.auth_token.delete()
	return Response([{"success" : "loged out succesfully"}])

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