from operator import ne
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from api.serializers import CandidatureSerializers
from .models import Candidature

import numpy as np
import pandas as pd
from keras.models import load_model

from .functions import PrepData

# Create your views here.


@api_view(['GET'])
def getAllCandidatures(request):
  queryset = Candidature.objects.all()

  serializer = CandidatureSerializers(queryset, many=True)
  return Response(serializer.data)


@api_view(['POST'])
def submitCandidature(request):

  try:

    data = request.data
    prediction = PrepData.submit_candidature(data)

    return JsonResponse(prediction, safe=False)

  except ValueError as e:
    return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
