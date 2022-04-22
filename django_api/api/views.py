import imp
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import CandidatureSerializers

from .models import Candidature

# Create your views here.


@api_view(['GET'])
def getAllCandidatures(request):
  queryset = Candidature.objects.all()

  serializer = CandidatureSerializers(queryset, many=True)
  return Response(serializer.data)
