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

from .functions.PrepData import scale_data

# Create your views here.


@api_view(['GET'])
def getAllCandidatures(request):
  queryset = Candidature.objects.all()

  serializer = CandidatureSerializers(queryset, many=True)
  return Response(serializer.data)


@api_view(['POST'])
def submitCandidature(request):

  try:

    mdl = load_model(
        'F:\\Visconti\\DevProgram\\Tutorial\\Django\\MachineLearning\\DjangoAPI_MachineLearning\\machine_learning\\model\\loan_model')

    # Grab the input data from the request, convert to DataFrame
    df_data = pd.DataFrame(request.data, index=[0])
    unit = scale_data(df_data)

    # Run model to predict
    y_pred = mdl.predict(unit)
    y_pred = (y_pred > 0.55)

    new_df = pd.DataFrame(y_pred, columns=['Status'])
    new_df = new_df.replace({True: 'Approved', False: 'Rejected'})

    return JsonResponse('Your Status is {}'.format(new_df), safe=False)

  except ValueError as e:
    return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
