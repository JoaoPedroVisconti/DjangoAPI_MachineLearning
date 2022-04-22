from operator import ne
from re import S
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

    # Candidature.objects.create(
    #     Dependents=data['Dependents'],
    #     ApplicantIncome=data['ApplicantIncome'],
    #     CoapplicantIncome=data['CoapplicantIncome'],
    #     LoanAmount=data['LoanAmount'],
    #     Loan_Amount_Term=data['Loan_Amount_Term'],
    #     Credit_History=data['Credit_History'],
    #     Gender=data['Gender'],
    #     Married=data['Married'],
    #     Education=data['Education'],
    #     Self_Employed=data['Self_Employed'],
    #     Property_Area=data['Property_Area'],
    # )

    # serializer = CandidatureSerializers(candidature, many=False)

    return JsonResponse(prediction, safe=False)

  except ValueError as e:
    return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
