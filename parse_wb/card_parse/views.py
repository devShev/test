from rest_framework import generics
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CardData
from .serializers import CardDataSerializer
from .tasks import parse_article


class ParseArticle(APIView):
    def post(
        self,
        request: Request,
        article: str,
    ) -> Response:
        parse_article.delay(article)
        return Response(status=status.HTTP_200_OK)


class CardDataListView(generics.ListAPIView):
    queryset = CardData.objects.all()
    serializer_class = CardDataSerializer
