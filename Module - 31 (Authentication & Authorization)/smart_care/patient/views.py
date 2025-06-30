from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers

# Create your views here.
class PatientViewset(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer


class RegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer


    def post(self, request):
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(user)
        return Response(serializer.errors)