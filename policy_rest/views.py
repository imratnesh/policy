from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Policy
from .serializers import PolicySerializer


# Create your views here.
class PolicyList(APIView):

    def get(self, request):
        policies = Policy.objects.all()
        ser = PolicySerializer(policies, many=True)
        return Response(ser.data)

    def post(self):
        pass
